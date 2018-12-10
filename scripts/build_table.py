"""
build a table of contents file called
notebook_list.md that has the sorted notebooks plus their urls
"""
import json
import pprint
import collections
import markdown_generator as mg
import pandas as pd
from pathlib import Path

lessons_file=Path(__file__).parent.parent / Path('docs/lesson_titles.json')
with open(lessons_file,'r') as f:
    lessons=json.load(f)

#
# make a pandas dataframe with the notebook filename, url etc.
#
root="https://github.com/phaustin/eosc213/blob/master"
tuple_dict=collections.defaultdict(list)
notebook_list=[]
for key,value in lessons.items():
    tuple_key=eval(key)
    new_value=[]
    url_path='/'.join(tuple_key)
    url_path='/'.join([root,url_path])
    for a_value in value:
        new_value=dict(zip(['title','filename'],a_value))
        new_value['url_path']='/'.join([url_path,new_value['filename']])
        for num in range(7):
            if key.find(f'L{num+1}') >=0:
                new_value['lesson_string']=f'Lesson {num+1}'
                new_value['lesson_num']=num+1
                break
        notebook_list.append(new_value)

#
# create the dataframe and sort on lesson number
#
notebooks_df = pd.DataFrame.from_records(notebook_list)
df=notebooks_df.sort_values('lesson_num')
df.to_csv('notebooks.csv',index=False)

#
# write the markdown table
#
outname="notebook_list.md"
outpath=lessons_file.parent / Path(outname)
with open(outpath, 'w') as f:
    writer = mg.Writer(f)
    table = mg.Table()
    table.add_column('Lesson')
    table.add_column('Description')
    table.add_column('Github link')
    for index,row in df.iterrows():
        a_row=row.to_dict()
        link = mg.link(a_row['url_path'],a_row['filename'])
        table.append(a_row['lesson_string'],a_row['title'],link)
    writer.write(table)

print(f"wrote the markdown file {str(outpath.resolve())}")


    


    
