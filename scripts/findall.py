"""
walk our directory tree and find every jupyter notebook, writing out
the location to a json file called out.json

out.json needs to be edited to add file descriptions, then is read in
by build_table.py to produce the table of contents

workflow:

python scripts/finall.py

edit scripts/out.json and save as "docs/lesson_titles.json"

then run:

python scripts/build_table.py

which produces docs/notebook_list.md

"""
import json
from collections import defaultdict
from pathlib import Path

jup_file_dict = defaultdict(lambda: defaultdict(dict))
#
# find the top directory, which is two levels up from this file
#
root = Path(__file__).parents[1]

#
# the loop below finds every file in the tree
# ending in .ipynb and records the full path as a tuple of folders
#
files = list(root.glob("**/*"))
jup_file_list = []
rst_file_list = []

for the_file in files:
    if the_file.is_file():
        if ".git" in the_file.parts:
            continue
        if str(the_file.name)[0] != ".":
            if the_file.suffix == ".ipynb":
                jup_file_list.append(tuple(the_file.parts))
            elif the_file.suffix == ".rst":
                rst_file_list.append(tuple(the_file.parts))
#
# use the path to make a dictionary key
#
jup_file_dict = defaultdict(list)
for a_tup in jup_file_list:
    jup_file_dict[a_tup[:-1]].append(a_tup[-1])

rst_file_dict = defaultdict(list)
for a_tup in rst_file_list:
    rst_file_dict[a_tup[:-1]].append(a_tup[-1])

#
# write out a json file so we can fill in the descriptions
# (i.e. the "tbd" entries"
#
key_list = []
value_list = []
for key, value in jup_file_dict.items():
    the_list = value
    new_list = [("tbd", item) for item in the_list]
    value_list.append(new_list)
    new_key = repr(key)
    key_list.append(new_key)

jup_file_dict = dict(zip(key_list, value_list))

rst_key_value_list = []
for key, value in rst_file_dict.items():
    lesson = key[-1]
    for item in value:
        rst_key_value_list.append((lesson, item))


outfile = "notebooks_out.json"
outpath = Path(__file__).parent.resolve() / Path(outfile)
with open(outpath, "w") as f:
    json.dump(jup_file_dict, f, indent=4)

rst_outfile = "rst_out.json"
rst_outpath = Path(__file__).parent.resolve() / Path(rst_outfile)
with open(rst_outpath, "w") as f:
    json.dump(rst_key_value_list, f, indent=4)


print(
    f"""
       wrote the files {str(outpath)} and {str(rst_outpath)}
       need to edit {str(outpath)} and save as docs/lesson_title.json
       then run build_table.py
      """
)
