import json
import pprint
import collections
import markdown_generator as mg
import pandas as pd

with open('lesson_titles.json','r') as f:
    lessons=json.load(f)

root="https://github.com/phaustin/eosc213/blob/test"
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

notebooks_df = pd.DataFrame.from_records(notebook_list)
df=notebooks_df.sort_values('lesson_num')
df.to_csv('notebooks.csv',index=False)

with open('notebook_list.md', 'w') as f:
    print('start')
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

    


    
