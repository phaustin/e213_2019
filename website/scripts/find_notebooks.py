#!/usr/bin/env python
"""
code to find notebooks

and try another line
"""
import json
import os
import shutil
import textwrap
from pathlib import Path

import context
from table import make_table


# def make_parser():
#     """
#     set up the command line arguments needed to call the program
#     """
#     linebreaks = argparse.RawTextHelpFormatter
#     parser = argparse.ArgumentParser(
#          formatter_class=linebreaks, description=__doc__.lstrip())
#     parser.add_argument('notebook_path', type=str, help='full path to notebook folder')
#     parser.add_argument("github_url", help="url for github repo")
#     return parser


def main(args=None):
    # print('PHA debug in main')
    # parser = make_parser()
    # args=parser.parse_args(args)
    #
    # find the notebooks list
    #
    root_dir = context.curr_dir.parents[1]
    website_dir = root_dir / Path("website")
    notebook_dir = root_dir / Path("notebooks")
    print(f"found notebook_dir {notebook_dir}")
    json_path = website_dir / Path("notebooks.json")
    with open(json_path, "r") as json_file:
        notebook_order = json.load(json_file)
    print(f"notebook order: {notebook_order}")
    txt_out = website_dir / Path("index_notebooks.txt")
    rst_out = website_dir / Path("notebook_index.rst")
    # print(f'here are the output files: {txt_out},{rst_out}')
    # print(f'DEBUG: here is the noteobok order from find_notebooks.py: \n{pprint.pformat(notebook_order)}\n')
    web_notebooks_path = website_dir / Path("web_notebooks")
    os.makedirs(web_notebooks_path, exist_ok=True)
    #
    # first line of table
    #
    table_list = [["notebook", "html", "python"]]
    namelist = []
    for week, weeklist in notebook_order.items():
        week_head = "**{}**".format(week)
        table_list.append([week_head, " ", " "])
        for notebook in weeklist:
            html_name = f"{notebook}.html"
            py_name = f"{notebook}.py"
            nb_name = f"{notebook}.ipynb"
            nb_file = list(notebook_dir.glob(f"**/{nb_name}"))[0]
            print(list(notebook_dir.glob(f"**/{html_name}"))[0].is_file())
            print(list(notebook_dir.glob(f"**/{py_name}"))[0].is_file())
            print(nb_file.is_file())
            shutil.copy(nb_file, web_notebooks_path)
            namelist.append(notebook)
            ipynb = r"`{}_ipynb`_"
            html = r"`{}_html`_"
            python = r"`{}_py`_"
            ipynb, html, python = [
                item.format(notebook) for item in [ipynb, html, python]
            ]
            table_list.append([ipynb, html, python])
    print(table_list)
    # #
    # # write out the shortcuts
    # #
    github_url = "https://github.com/phaustin"
    with open(txt_out, "w") as notetxt:
        print(f"writing {str(txt_out.resolve())}")
        for name in namelist:
            notetxt.write(
                f".. _{name}_ipynb: {github_url}/blob/master/notebooks/{name}.ipynb\n"
            )
            notetxt.write(f".. _{name}_html: html/{name}.html\n")
            notetxt.write(
                f".. _{name}_py: {github_url}/blob/master/notebooks/python/{name}.py\n"
            )

    header = """
    .. include:: index_notebooks.txt

    .. _notebooks:

    E213 notebooks in order of appearance
    =====================================

    """

    header = textwrap.dedent(header)
    # pdb.set_trace()
    with open(rst_out, "w") as noterst:
        print(f"writing {str(rst_out.resolve())}")
        noterst.write(header)
        noterst.write(make_table(table_list))


if __name__ == "__main__":
    main()
