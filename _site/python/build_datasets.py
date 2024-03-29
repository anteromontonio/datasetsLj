from typing import Dict, List, Tuple

import os
from pathlib import Path
import pandas as pd
import numpy as np
#this is a change

# This is kind of the main routine, it is used to build a dataset website from a csvfile
# def build_pages_for_dataset(
#         csv_file: str, #name of the csv_file without extension
#         dataset_id: str, #inner id for the dataset, eg. "chiralMaps"
#         dataset_title: str, #actual title to be displayed on the website, eg. "Chiral maps up to 6000 edges"
#         max_rows :int =10000,
# ) -> None :
    
#     dataSet=pd.read_csv(f"../csv/{csv_file}.csv")#reads csv file
#     preprocess_DataSet(dataSet)
    
#     if not os.path.exists(f'../{dataset_id}'):
#         os.mkdir(f'../{dataset_id}')

#     build_tables_from_csv(data,max_rows,dataset_id,dataset_title)
#     if not os.path.exists(f'../_datasets/{dataset_id}.md'): #only runs if the file does not exists, to avoid overwriting
#         build_dataset_page(dataset_id,dataset_title)


def build_tables_from_csv(
  data, #pandas dataset
  dataset_id: str, #inner id for the dataset, eg. "chiralMaps"
  dataset_title: str, #actual title (on the website) eg "Chiral maps up to 6000 edges"
  toShowInTables: List,
  max_rows: int = 10000, 
 ) -> None :
    data_split_list=[]
    for i in range(len(data)//max_rows):
        data_split_list.append(data.iloc[max_rows*i:max_rows*(i+1)])
    data_split_list.append(data.iloc[max_rows*(len(data)//max_rows):])

    for i in range(len(data_split_list)):
        frontmatter=f'---\nlayout: default\ndataset: {dataset_id}\ndataset_title: {dataset_title}\npermalink: /{dataset_id}/{dataset_id}_tab_{i} \nfirst_entry: {data_split_list[i].iat[0,0]}\nlast_entry: {data_split_list[i].iat[-1,0]}\n---\n\n'
        html=data_split_list[i].to_html(index=False, columns=toShowInTables,)
        html=html.replace('border="1"', 'id="myTable"')
        html=html.replace('class="dataframe"','class="display compact" style="width=100%"')
        html=html.replace('style="text-align: right;"','')
        with open(f'../_tables/{dataset_id}_tab_{i}.md', 'w') as md_file:
            md_file.write(frontmatter)
            md_file.write(f"The following table contains the entries from {{{{ page.first_entry }}}} to {{{{ page.last_entry }}}} of the dataset of [{{{{ page.dataset_title }}}}]( /datasets/{dataset_id} ).\n ")
            md_file.write(html)
        add_links_to_tables(f'{dataset_id}_tab_{i}',data_split_list[i])

def build_dataset_page(
  dataset_id: str, #inner id for the dataset, eg. "chiralMaps"
  dataset_title: str, #actual title (on the website) eg "Chiral maps up to 6000 edges"
  toHumanDict: Dict, #A dictionary translating the information to human readable information.
  res:str = "", #you can add a string with resources (link to gap packages, documentation, etc)... 
  overwrite:bool = False, # to force overwriting
) -> None:
    if not os.path.exists(f'../_datasets/{dataset_id}.md') or overwrite:
        with open(f'../_datasets/{dataset_id}.md', 'w') as dataset_md:             
            frontmatter=f"--- \n layout: page\n title: {dataset_title}\n permalink: /{dataset_id}/\n---\n\n"
            
            tables=f"### Tables \n<ol>\n{{% for post in site.tables %}}\n  {{% if post.dataset == '{dataset_id}' %}}\n <li> A <a href= \"{{{{ site.url }}}}{{{{ post.url | relative_url }}}}\" > table </a> containing the entries from {{{{ post.first_entry }}}} to {{{{ post.last_entry }}}} </li>\n{{% endif %}}{{% endfor %}} \n </ol>\n\n"

            resources="### Resources" + res + "\n\n"

            dictContents="This dataset contains (at least) the following information for every entry:\n"

            for k in toHumanDict:
                if len(toHumanDict[k])>1 and not isinstance(toHumanDict[k], str):
                    dictContents= dictContents+"- **"+ k +"**: " + toHumanDict[k][0]+"\n"
                else:
                    dictContents= dictContents+"- **"+ k +"**: " + toHumanDict[k]+"\n"

            md_text=frontmatter + "\n"+dictContents + "\n" + resources +"\n"+ tables
            dataset_md.write(md_text)
#end of build dataset page

def populate_a_dataEntry_page(
    dataEntry, #an entry o pandas
    toHumanDict: Dict, #a dictionary with the columns of the dataset translated to readable language
    dataset_id: str, #the id of the dataset which it belongs
    dataset_title: str #actual title (on the website) eg "Chiral maps up to 6000 edges"
) -> None:
    dataDict=dataEntry.to_dict()
    frontmatter=f'--- \n permalink: /{dataset_id}/{dataEntry.ID_url} \n collection: {dataset_id}\n layout: dataEntry\n title: {dataset_title} - {dataEntry.ID}\n---\n\n'
    with open(f'../_{dataset_id}/{dataEntry.ID_url}.md', 'w') as md_file:
        md_file.write(frontmatter)
        #iterate over the entries of the dictionary and populate
        for k in toHumanDict:
            if len(toHumanDict[k])>1 and not isinstance(toHumanDict[k], str):
                md_file.write("- **"+toHumanDict[k][0]+"**: ["+str(dataDict[k])+"]({{ site.url }}/"+toHumanDict[k][1]+ str(dataDict[k+"_url"])+")\n")
            else:
                md_file.write("- **"+toHumanDict[k]+"**: "+str(dataDict[k])+"\n")

def create_dataPages_for_Dataset(
    dataset_id:str, #dataset_id
    dataSet, #a pandas Dataset
    dataset_title: str, #actual title (on the website) eg "Chiral maps up to 6000 edges"
    toHumanDict: Dict, #a dictionary with the columns of the dataset translated to readable language
) -> None:
  if not os.path.exists(f'../_{dataset_id}'):
        os.mkdir(f'../_{dataset_id}')
  for index,data in dataSet.iterrows():
      populate_a_dataEntry_page(data,toHumanDict,dataset_id,dataset_title)

def preprocess_DataSet(
    dataset, #a pandas dataset
    cols_to_url: List, #columns that need to be url-ised
)->None:
    dataset.replace(np.nan, '', regex=True)
    for col in cols_to_url:
        if col in dataset.columns:
            dataset[col+"_url"]=dataset[col].str.replace("[","_")
            dataset[col+"_url"]=dataset[col+"_url"].str.replace(";","_")
            dataset[col+"_url"]=dataset[col+"_url"].str.replace("]","")

def add_links_to_tables(
    table_file:str, #path to the table file
    dataset, #pandas dataset with url-s columns
) -> None:
    
    with open(f'../_tables/{table_file}.md', 'r') as tableF:
        contents=tableF.read()
        for index,row in dataset.iterrows():
            link_str=f'<a href="./{str(row.ID_url)}.html"> {str(row.ID)}</a>'
            contents=contents.replace(str(row.ID),link_str)
    with open(f'../_tables/{table_file}.md', 'w') as tableF:
       tableF.write(contents)