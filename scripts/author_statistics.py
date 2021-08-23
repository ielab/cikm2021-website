from collections import OrderedDict

import pandas as pd
import xmltodict
import yaml

with open("scripts/output.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
df = pd.DataFrame(data_dict["erights_record"]["paper"])
#%%
df.rename(columns={"#": "Id"}, inplace=True)


#%%


def get_item(item):
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

        yield {
            "paper_title": item.paper_title,
            "paper_type": item.paper_type,
            "author": " ".join(name),
            "affiliation": author["affiliations"]["affiliation"],
            "country": author["country"],
        }


l = [get_item(x) for x in df.to_records()]
df_stats = pd.DataFrame([x for y in l for x in y])
# total count
df_stats.author.value_counts().to_excel("author_counts_total.xlsx")
#%%
df_stats_total = df_stats.author.value_counts().reset_index(name="total_count")
df_stats_full = (
    df_stats[df_stats.paper_type == "Full"]
    .author.value_counts()
    .reset_index(name="full_count")
)
df_stats_short = (
    df_stats[df_stats.paper_type == "Short"]
    .author.value_counts()
    .reset_index(name="short_count")
)
df_stats_applied = (
    df_stats[df_stats.paper_type == "Applied"]
    .author.value_counts()
    .reset_index(name="applied_count")
)
df_stats_demo = (
    df_stats[df_stats.paper_type == "Demo"]
    .author.value_counts()
    .reset_index(name="demo_count")
)
df_stats_resource = (
    df_stats[df_stats.paper_type == "Resource"]
    .author.value_counts()
    .reset_index(name="resource_count")
)
df_stats_tutorial = (
    df_stats[df_stats.paper_type == "Tutorial"]
    .author.value_counts()
    .reset_index(name="tutorial_count")
)
df_all = pd.merge(
    pd.merge(
        pd.merge(
            pd.merge(
                pd.merge(
                    pd.merge(df_stats_full, df_stats_short, how="outer"),
                    df_stats_applied,
                    how="outer",
                ),
                df_stats_demo,
                how="outer",
            ),
            df_stats_resource,
            how="outer",
        ),
        df_stats_tutorial,
        how="outer",
    ),
    df_stats_total,
    how="outer",
).fillna(0).sort_values(by="total_count", ascending=False)
print(df_all)
df_all.to_excel("author_counts.xlsx")
#%%
