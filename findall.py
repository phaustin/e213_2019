from pathlib import Path
import pprint
from collections import defaultdict
import json

file_dict = defaultdict(lambda: defaultdict(dict))

files=list(Path().glob("**/*"))
file_list=[]

for the_file in files:
    if the_file.is_file():
        if ".git" in the_file.parts:
            continue
        if str(the_file.name)[0]!=".":
            if the_file.suffix=='.ipynb':
                file_list.append(tuple(the_file.parts))

file_dict=defaultdict(list)
for a_tup in file_list:
    file_dict[a_tup[:-1]].append(a_tup[-1])

key_list=[]
value_list=[]
for key,value in file_dict.items():
    the_list=value
    new_list=[("tbd",item) for item in the_list]
    value_list.append(new_list)
    new_key=repr(key)
    key_list.append(new_key)

file_dict=dict(zip(key_list,value_list))    
    
pprint.pprint(dict(file_dict))

with open('out.json','w') as f:
    json.dump(file_dict,f,indent=4)
    
