---
# DO NOT MANUALLY EDIT THIS FILE.
layout: default
---

# Organisation Committee
{% for chair in site.data.oc.chairs %}
<div class="row">
<h2>{{ chair.name }}</h2>
{% for member in chair.members %}
<div class="col-sm-3 col-md-3 col-lg-3">
    <div class="thumbnail">
{%- if member.img -%}
      <img src="{{- member.img -}}" alt="{{- member.name -}}" style="object-fit: cover; height:160px; width:100%;">
{%- else -%}
      <img src="/img/oc/default.png" alt="{{- member.name -}}" style="object-fit: cover; height:160px; width:100%;">
{%- endif -%}      
      <div class="caption">      
        <p>{{- member.name -}}</p>
      </div>
    </div>
</div>    
{% endfor %}
</div>
{% endfor %}