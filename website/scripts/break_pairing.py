"""
add the nbsphinx metadata tag {"execute": "never"} to
a notebook's metadata

"jupytext": {"formats": "ipynb"}

usage:  python add_nbsphinx_meta.py 1-python-basics.ipynb nb_folder="."

this modifies 1-python-basics.ipynb inplace and also puts a copy in
eosc213/website/web_notebooks  so nbsphinx will pick it up in the sphinx-build
and not try to run it.

"""
import argparse
import shutil
from pathlib import Path

import context
import nbformat


def add_meta(nb_name, nb_folder=None):
    if nb_folder is None:
        nb_file = list(context.student_dir.glob(f"**/{nb_name}"))[0]
        if nb_file.is_file():
            print(f"working with {nb_file}")
        else:
            raise ValueError(f"could not find {nb_file}")
        the_folder = nb_file.parent
    else:
        nb_file = Path(nb_folder) / Path(nb_name)
        the_folder = nb_file.parent
        if nb_file.is_file():
            print(f"working with {nb_file}")
        else:
            raise ValueError(f"could not find {nb_file} in {nb_folder}")
    with open(nb_file, "r") as f:
        nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)
    nbsphinx = nbformat.from_dict({"execute": "never"})
    nb["metadata"]["nbsphinx"] = nbsphinx
    outfile = the_folder / Path("temporary_notebook.ipynb")
    if outfile.is_file():
        outfile.unlink()
    with open(outfile, "w") as f:
        nbformat.write(nb, f, version=nbformat.NO_CONVERT)
    print(f"wrote new file {outfile}")
    shutil.copy(outfile, nb_file)
    web_notebooks = context.website_dir / Path("web_notebooks")
    shutil.copy(outfile, nb_file)
    try:
        shutil.copy(outfile, web_notebooks)
    except shutil.SameFileError:
        pass
    print(f"overwrote {nb_file}")
    return outfile


def make_parser():
    """
    set up the command line arguments needed to call the program
    """
    linebreaks = argparse.RawTextHelpFormatter
    parser = argparse.ArgumentParser(
        formatter_class=linebreaks, description=__doc__.lstrip()
    )
    help_message = "name of the  notebook to be modified"
    parser.add_argument("notebook_name", type=str, help=help_message)
    help_message = """path to the notebook. Optional,
                      defaults to the
                      Nextcloud/213/graded_assignments/release
                      folder"""
    parser.add_argument(
        "-d", action="store", dest="notebook_dir", type=str, help=help_message
    )
    return parser


def main(args=None):
    parser = make_parser()
    args = parser.parse_args(args)
    add_meta(args.notebook_name, nb_folder=args.notebook_dir)


if __name__ == "__main__":
    main()
