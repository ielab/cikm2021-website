---
layout: default
best-papers:
 - rgfp1290
 - afp0975
 - rgsp2949
runner-ups:
 - rgfp0090
 - rgfp0032
 - afp1012
 - afp1085
 - rgsp2332
full-papers:
 - rgfp1290
 - rgfp0090
 - rgfp0032
 - rgfp0977
 - rgfp0111
applied-papers:
 - afp0975
 - afp1012
 - afp1085
 - afp0286
 - afp1567
short-papers:
 - rgsp2949
 - rgsp2332
 - rgsp2596
 - rgsp2654
 - rgsp2725
 - rgsp2940
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
<li>{%-if page.best-papers contains paper.acm_id -%}<span class="label label-warning">best paper</span>&nbsp;{%-endif-%}{%-if page.runner-ups contains paper.acm_id -%}<span class="label label-success">runner up</span>&nbsp;{%-endif-%}{% include paper.html paper=paper %}</li>
{% endfor %}
</ul>

## Applied Papers
<ul>
{% for paper_id in page.applied-papers %}
{% assign paper = site.data.accepted-papers.applied-papers | where_exp: "item", "item.acm_id == paper_id" | first %}
<li>{%-if page.best-papers contains paper.acm_id -%}<span class="label label-warning">best paper</span>&nbsp;{%-endif-%}{%-if page.runner-ups contains paper.acm_id -%}<span class="label label-success">runner up</span>&nbsp;{%-endif-%}{% include paper.html paper=paper %}</li>
{% endfor %}
</ul>

## Short Papers
<ul>
{% for paper_id in page.short-papers %}
{% assign paper = site.data.accepted-papers.short-papers | where_exp: "item", "item.acm_id == paper_id" | first %}
<li>{%-if page.best-papers contains paper.acm_id -%}<span class="label label-warning">best paper</span>&nbsp;{%-endif-%}{%-if page.runner-ups contains paper.acm_id -%}<span class="label label-success">runner up</span>&nbsp;{%-endif-%}{% include paper.html paper=paper %}</li>
{% endfor %}
</ul>

## Resource Papers
<ul>
{% for paper_id in page.resource-papers %}
{% assign paper = site.data.accepted-papers.resource-papers | where_exp: "item", "item.acm_id == paper_id" | first %}
<li>{%-if page.best-papers contains paper.acm_id -%}<span class="label label-warning">best paper</span>&nbsp;{%-endif-%}{%-if page.runner-ups contains paper.acm_id -%}<span class="label label-success">runner up</span>&nbsp;{%-endif-%}{% include paper.html paper=paper %}</li>
{% endfor %}
</ul>

## Demo Papers
<ul>
{% for paper_id in page.demo-papers %}
{% assign paper = site.data.accepted-papers.demo-papers | where_exp: "item", "item.acm_id == paper_id" | first %}
<li>{%-if page.best-papers contains paper.acm_id -%}<span class="label label-warning">best paper</span>&nbsp;{%-endif-%}{%-if page.runner-ups contains paper.acm_id -%}<span class="label label-success">runner up</span>&nbsp;{%-endif-%}{% include paper.html paper=paper %}</li>
{% endfor %}
</ul>
