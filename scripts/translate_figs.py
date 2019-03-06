"""
Usage:  python translate_figs.py notebook.py

Given a jupytext python:percent notebook,
change all occurances of an image tag like:

<img src="figures/2d_flux.png" alt="pic05" width="20%" >

to a python Image call like this:

# Image(figures/2d_flux.png){width="20%"}

and write it out as a new file called notebook_nbsphinx.py
along with a translated notebook notebook_nbsphinx.ipynb
"""
import argparse
import json
import pdb
import re
import sys
from pathlib import Path

import jupytext
import nbformat
from bs4 import BeautifulSoup
from jupytext.formats import JUPYTEXT_FORMATS
from jupytext.formats import rearrange_jupytext_metadata
from jupytext.jupytext import writes
from nbconvert.preprocessors import CellExecutionError
from nbconvert.preprocessors import ExecutePreprocessor
from nbformat.v4.nbbase import new_code_cell
from nbformat.v4.nbbase import new_markdown_cell
from nbformat.v4.nbbase import new_notebook

split_cell_re = re.compile(r"(.*)(#\s+.*\<img\s+src.*\>)(.*)", re.DOTALL)
image_re = re.compile(r"#\s+.*(\<img.*\>).*")
image_re = re.compile(r".*(\<img\s+src.*\>).*")
template = '# ![{alt:}]({src:}){{width="{width:}"}}\n'
py_template = 'Image("{src:}",width="{width:}")\n'

toc_meta = {
    "toc": {
        "base_numbering": 1,
        "nav_menu": {},
        "number_sections": True,
        "sideBar": True,
        "skip_h1_title": True,
        "title_cell": "Table of Contents",
        "title_sidebar": "Contents",
        "toc_cell": True,
        "toc_position": {},
        "toc_section_display": True,
        "toc_window_display": True,
    }
}

fmt_dict = {item.format_name: item for item in JUPYTEXT_FORMATS}


def make_parser():
    """
    set up the command line arguments needed to call the program
    """
    linebreaks = argparse.RawTextHelpFormatter
    parser = argparse.ArgumentParser(
        formatter_class=linebreaks, description=__doc__.lstrip()
    )
    parser.add_argument("infile", type=str, help="name of pytnon notebook")
    return parser


def main(args=None):
    parser = make_parser()
    args = parser.parse_args(args)
    infile = Path(args.infile).resolve()
    in_dir = infile.parent
    py_outfile = in_dir / f"{infile.stem}_nbsphinx.py"
    nb_outfile = in_dir.parent / f"{infile.stem}_nbsphinx.ipynb"
    print(f"writing:\n{py_outfile}\n{nb_outfile}")
    with open(infile, "r") as input_file:
        in_py = input_file.readlines()

    # collect = ""
    # for the_line in in_py:
    #     match = image_re.match(the_line)
    #     if match:
    #         text = match.group(1)
    #         soup = BeautifulSoup(text, "html.parser")
    #         out = soup()
    #         md_image = template.format_map(out[0].attrs)
    #         collect += md_image
    #     else:
    #         collect += the_line

    # with open(py_outfile, "w") as output_file:
    #     output_file.write(collect)

    # with open(nb_outfile, "w") as output_file:
    #     nb = jupytext.readf(py_outfile)
    #     jupytext.writef(nb, nb_outfile, fmt="ipynb")

    orig_nb = jupytext.readf(infile)

    split_cell_re = re.compile(
        r"^(?P<front>.*?)(?P<img>\<img\s+src.*\>)(?P<back>.*?)", re.DOTALL
    )
    need_display_import = True
    new_nb_cells = list(orig_nb.cells)
    for index, item in enumerate(orig_nb.cells):
        print(f"at cell {index}")
        item["metadata"]["cell_count"] = index
        if item["cell_type"] == "markdown":
            text = item["source"]
            if text.find("pic") > -1:
                print(f"found img for: {text[:20]}")
            out = split_cell_re.match(text)
            if out:
                print(f"length of split is {len(out.groups())}")
                print(f"splitting cell at index {index}")
                cell_dict = dict()
                for name in ["front", "back"]:
                    src = out.group(name)
                    if len(src) > 0:
                        cell_dict[name] = new_markdown_cell(source=src)
                src = out.group("img")
                match = image_re.match(src)
                if match:
                    text = match.group(1)
                    soup = BeautifulSoup(text, "html.parser")
                    out = soup()
                    py_image = py_template.format_map(out[0].attrs)
                cell_dict["img"] = new_code_cell(source=py_image)
                count = 0
                for key in ["front", "img", "back"]:
                    try:
                        if key == "front":
                            new_nb_cells[index] = cell_dict[key]
                        else:
                            new_nb_cells.insert(index + count, cell_dict[key])
                            count += 1
                    except KeyError:
                        pass
        else:
            item["metadata"]["cell_count"] = index
            if item["source"].find("IPython.display") > -1:
                need_display_import = False
            print(f"found python cell: {item['source']}")
    if need_display_import:
        top_cell = new_code_cell(source="from IPython.display import Image")
        new_nb_cells.insert(1, top_cell)
    orig_nb.cells = new_nb_cells
    # https://nbconvert.readthedocs.io/en/latest/execute_api.html
    print(f"running notebook in folder {nb_outfile.parent}")
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3", allow_errors=True)
    path = str(nb_outfile.parent)
    path_dict = dict({"metadata": {"path": path}})
    try:
        out = ep.preprocess(orig_nb, path_dict)
    except CellExecutionError:
        out = None
        msg = f"Error executing the notebook {nb_outfile.name}.\n\n"
        msg += f"See notebook {nb_outfile.name} for the traceback."
        print(msg)
        raise
    finally:
        if "toc" not in orig_nb["metadata"]:
            orig_nb["metadata"].update(toc_meta)
            pdb.set_trace()
            rearrange_jupytext_metadata(orig_nb["metadata"])
            out = writes(orig_nb, "py", nbformat.NO_CONVERT)
            pdb.set_trace()
        with open(nb_outfile, mode="wt") as f:
            nbformat.write(orig_nb, f)
        jupytext.writef(orig_nb, py_outfile, fmt="py")

    print(f"wrote {nb_outfile} and \n {py_outfile}")


if __name__ == "__main__":
    #
    # will exit with non-zero return value if exceptions occur
    #
    # args = ['vancouver_hires.h5']
    sys.exit(main())
