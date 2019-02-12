"""
Usage:  python translate_figs.py notebook.py

Given a jupytext python:percent notebook,
change all occurances of an image tag like:

<img src="figures/2d_flux.png" alt="pic05" width="20%" >

to a markdown figure refernce like

# ![pic05](figures/2d_flux.png){width="20%"}

and write it out as a new file called notebook_nbsphinx.py
along with a translated notebook notebook_nbsphinx.ipynb
"""
import re
import sys
from pathlib import Path

import jupytext
from bs4 import BeautifulSoup

split_cell_re = re.compile(r"(.*)(#\s+.*\<img\s+src.*\>)(.*)", re.DOTALL)
image_re = re.compile(r"#\s+.*(\<img\s+src.*\>).*")
template = '# ![{alt:}]({src:}){{width="{width:}"}}\n'

print(sys.argv)
print(f"here is current directory: {Path()}")

infile = Path(sys.argv[1]).resolve()
in_dir = infile.parent
py_outfile = in_dir / f"{infile.stem}_nbsphinx.py"
nb_outfile = in_dir.parent / f"{infile.stem}_nbsphinx.ipynb"
print(f"writing:\n{py_outfile}\n{nb_outfile}")
with open(infile, "r") as input_file:
    in_py = input_file.readlines()

collect = ""
for the_line in in_py:
    match = image_re.match(the_line)
    if match:
        text = match.group(1)
        soup = BeautifulSoup(text, "html.parser")
        out = soup()
        md_image = template.format_map(out[0].attrs)
        collect += md_image
    else:
        collect += the_line

with open(py_outfile, "w") as output_file:
    output_file.write(collect)

with open(nb_outfile, "w") as output_file:
    nb = jupytext.readf(py_outfile)
    jupytext.writef(nb, nb_outfile, fmt="ipynb")

# orig_nb = jupytext.readf(infile)

# split_cell_re=re.compile(r"^(?P<front>.*?)(?P<img>\<img\s+src.*\>)(?P<back>.*?)",re.DOTALL)
# keep_dict=dict()
# for index, item in enumerate(orig_nb.cells):
#     if item['cell_type'] == 'markdown':
#         text=item['source']
#         out=split_cell_re.match(text)
#         if out:
#             cell_dict=dict()
#             for name in ['front','back']:
#                 src=out.group(name)
#                 if len(src) > 0:
#                     cell_dict[name]=new_markdown_cell(source=src)
#             src=out.group('img')
#             cell_dict['img']=new_code_cell(source=src)
#             keep_dict[index]=cell_dict
# cell_list=list(keep_dict.keys())
# cell_list=cell_list[::-1]
# print(cell_list)

# for index in cell_list:
#     next_cell=index
#     try:
#         orig_nb.cells.insert(next_cell,keep_dict[index]['front'])
#         next_cell+=1
#     except:
#         pass
#     orig_nb.cells.insert(next_cell,keep_dict[index]['img'])
#     next_cell+=1
#     try:
#         orig_nb.cells.insert(next_cell,keep_dict[index]['back'])
#     except:
#         pass

# nb_tryfile = in_dir / f"{infile.stem}_nbtry.ipynb"
# jupytext.writef(orig_nb,nb_tryfile,fmt="ipynb")

# nb_tryfile = in_dir / "python"  / f"{infile.stem}_nbtry.py"
# jupytext.writef(orig_nb,nb_tryfile,fmt="percent")
