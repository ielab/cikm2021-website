---
layout: default
full-papers:
 - rgfp0090
 - rgfp1290
 - rgfp0977
 - rgfp0111
 - rgfp0032
applied-papers:
 - afp0286
 - afp0975
 - afp1012
 - afp1085
 - afp1567
short-papers:
 - rgsp2332
 - rgsp2596
 - rgsp2654
 - rgsp2725
 - rgsp2940
 - rgsp2949
resource-papers:
 - rsfp1460
 - rsfp3057
 - rsfp3066
demo-papers:
 - de3059
 - de3075
 - de3094
 - de3068
 - de3089
---

# Best Paper Nominations

## Full Papers
<ul>
{% for paper_id in page.full-papers %}
{% assign paper = site.data.accepted-papers.full-papers | where_exp: "item", "item.acm_id == paper_id" | first %}
<li>{% include paper.html paper=paper %}</li>
{% endfor %}
</ul>

## Applied Papers
<ul>
{% for paper_id in page.applied-papers %}
{% assign paper = site.data.accepted-papers.applied-papers | where_exp: "item", "item.acm_id == paper_id" | first %}
<li>{% include paper.html paper=paper %}</li>
{% endfor %}
</ul>

## Short Papers
<ul>
{% for paper_id in page.short-papers %}
{% assign paper = site.data.accepted-papers.short-papers | where_exp: "item", "item.acm_id == paper_id" | first %}
<li>{% include paper.html paper=paper %}</li>
{% endfor %}
</ul>

## Resource Papers
<ul>
{% for paper_id in page.resource-papers %}
{% assign paper = site.data.accepted-papers.resource-papers | where_exp: "item", "item.acm_id == paper_id" | first %}
<li>{% include paper.html paper=paper %}</li>
{% endfor %}
</ul>

## Demo Papers
<ul>
{% for paper_id in page.demo-papers %}
{% assign paper = site.data.accepted-papers.demo-papers | where_exp: "item", "item.acm_id == paper_id" | first %}
<li>{% include paper.html paper=paper %}</li>
{% endfor %}
</ul>
