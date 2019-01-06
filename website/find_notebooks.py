#!/usr/bin/env python
"""
code to find notebooks

and try another line
"""
from pathlib import Path
from pyutils.table import make_table
from collections import OrderedDict
import argparse
import pdb
import textwrap
import importlib_resources as ir
import context
import json
import pprint

def make_parser():
    """
    set up the command line arguments needed to call the program
    """
    linebreaks = argparse.RawTextHelpFormatter
    parser = argparse.ArgumentParser(
         formatter_class=linebreaks, description=__doc__.lstrip())
    parser.add_argument('notebook_path', type=str, help='full path to notebook folder')
    parser.add_argument("github_url", help="url for github repo")
    return parser


def main(args=None):
    print('PHA debug in main')
    parser = make_parser()
    args=parser.parse_args(args)
    with ir.path('coursebuild','notebooks.json') as path:
        with open(path,'r') as json_file:
            notebook_order=json.load(json_file,object_pairs_hook=OrderedDict)
        txt_out = Path(__file__).parent / Path('index_notebooks.txt')
        rst_out = Path(__file__).parent / Path('notebook_index.rst')
        print(f'here are the output files: {txt_out},{rst_out}')
    print(f'DEBUG: here is the noteobok order from find_notebooks.py: \n{pprint.pformat(notebook_order)}\n')

    the_path = Path(args.notebook_path)
    html_files=the_path.glob('**/html/*html')

    for item in html_files:
        print(item.stem,item.root,str(item))

    #
    # first line of table
    #
    table_list=[['notebook','html','python']]
    namelist=[]
    for week,weeklist in notebook_order.items():
        week_head = '**{}**'.format(week)
        table_list.append([week_head," "," "])
        for notebook in weeklist:
            namelist.append(notebook)
            ipynb=r"`{}_ipynb`_"
            html=r"`{}_html`_"
            python = r"`{}_py`_"
            #print('!!!!! table entry for: ',html)
            ipynb,html,python = [item.format(notebook) for item in [ipynb,html,python]]
            table_list.append([ipynb,html,python])
    #
    # write out the shortcuts
    #
    with open(txt_out,'w') as notetxt:
        print(f'writing {str(txt_out.resolve())}')
        for name in namelist:
           notetxt.write(f'.. _{name}_ipynb: {args.github_url}/blob/master/notebooks/{name}.ipynb\n')
           notetxt.write(f'.. _{name}_html: html/{name}.html\n')
           notetxt.write(f'.. _{name}_py: {args.github_url}/blob/master/notebooks/python/{name}.py\n')

    header="""
    .. include:: index_notebooks.txt             

    .. _notebooks:

    A301 notebooks in order of appearance
    =====================================

    """

    header = textwrap.dedent(header)
    #pdb.set_trace()
    with open(rst_out,'w') as noterst:
        print(f'writing {str(rst_out.resolve())}')
        noterst.write(header)
        noterst.write(make_table(table_list))

if __name__ == "__main__":
    main()
    
