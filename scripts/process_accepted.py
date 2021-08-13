from collections import OrderedDict

import pandas as pd
import xmltodict
import yaml

with open("scripts/output.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
df = pd.DataFrame(data_dict["erights_record"]["paper"])
#%%
df.rename(columns={"#": "Id"}, inplace=True)
full_papers = df[df.paper_type == "Full"]
applied_papers = df[df.paper_type == "Applied"]
short_papers = df[df.paper_type == "Short"]
resource_papers = df[df.paper_type == "Resource"]
demo_papers = df[df.paper_type == "Demo"]
tutorials = df[df.paper_type == "Tutorial"]

#%%


def get_item(item):
    authors = []
    for author in item.authors["author"]:
        name = []
        if not isinstance(author, OrderedDict):
            continue
        if author["first_name"] is not None:
            name.append(author["first_name"])
        if author["middle_name"] is not None:
            name.append(author["middle_name"])
        if author["last_name"] is not None:
            name.append(author["last_name"])

        authors.append(
            {
                "name": " ".join(name),
                "affiliation": author["affiliations"]["affiliation"],
                "country": author["country"],
            }
        )
    return {"title": item.paper_title, "authors": authors}


papers = {
    "full-papers": [get_item(x) for x in full_papers.to_records()],
    "applied-papers": [get_item(x) for x in applied_papers.to_records()],
    "short-papers": [get_item(x) for x in short_papers.to_records()],
    "resource-papers": [get_item(x) for x in resource_papers.to_records()],
    "demo-papers": [get_item(x) for x in demo_papers.to_records()],
    "tutorials": [get_item(x) for x in tutorials.to_records()],
}

with open("_data/accepted-papers.yml", "w+") as f:
    f.write(yaml.dump(papers, default_flow_style=False))
#%%
