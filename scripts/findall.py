"""
walk our directory tree and find every jupyter notebook, writing out
the location to a json file called out.json

out.json needs to be edited to add file descriptions, then is read in
by build_table.py to produce the table of contents

workflow:

python scripts/finall.py

edit out.json and save ass "lesson_titles.json"

python scripts/build_table.py

"""

from pathlib import Path
import pprint
from collections import defaultdict
import json

file_dict = defaultdict(lambda: defaultdict(dict))
#
# find the top directory, which is one level up from this file
#
root=Path(__file__).parent.parent

#
# the loop below finds every file in the tree
# ending in .ipynb and records the full path as a tuple of folders
#
files=list(root.glob("**/*"))
file_list=[]

for the_file in files:
    if the_file.is_file():
        if ".git" in the_file.parts:
            continue
        if str(the_file.name)[0]!=".":
            if the_file.suffix=='.ipynb':
                file_list.append(tuple(the_file.parts))

#
# use the path to make a dictionary key
#
file_dict=defaultdict(list)
for a_tup in file_list:
    file_dict[a_tup[:-1]].append(a_tup[-1])

#
# write out a json file so we can fill in the descriptions
# (i.e. the "tbd" entries"
#
key_list=[]
value_list=[]
for key,value in file_dict.items():
    the_list=value
    new_list=[("tbd",item) for item in the_list]
    value_list.append(new_list)
    new_key=repr(key)
    key_list.append(new_key)

file_dict=dict(zip(key_list,value_list))    
    
#pprint.pprint(dict(file_dict))

outfile="out.json"
outpath=Path(__file__).parent.resolve() / Path(outfile)
with open(outpath,'w') as f:
    json.dump(file_dict,f,indent=4)

print(f"wrote the file {str(outpath)}\n"
      "now edit this and save as docs/lesson_title.json\n"
      "then run build_table.py")
    
