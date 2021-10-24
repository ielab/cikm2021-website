---
layout: fullwidth
---

# Keynotes

<div class="container">
{% for speaker in site.data.keynotes.speakers %}
    {%- if speaker.abstract -%}
    <h2>{{speaker.title}}</h2>
    <div class="row">
        <div class="col-md-6">                
            <p><b class="text-uppercase">abstract</b>&nbsp;{{-speaker.abstract-}}</p>
        </div>
        <div class="col-md-6">       
            <p><b class="text-uppercase">bio</b>&nbsp;{{-speaker.bio-}}</p>
            <div class="thumbnail" style="width:160px; float: inline-start; margin-right: 32px">
                  <img src="{{speaker.image}}" alt="Supplied image of {{ speaker.name }}" style="object-fit: cover; height:160px; width:100%;">
                  <div class="caption">      
                    <p><b>{{- speaker.name -}}</b></p>
                    <p>{{- speaker.organisation -}}</p>
                  </div>
            </div>                
            <p><b class="text-uppercase">links</b></p>
            <ul style="list-style: inside">
                {%- if speaker.abstract_link -%}<li><a href="{{speaker.abstract_link}}">Download abstract</a></li>{%- endif -%} 
                <li><a href="{{speaker.website}}">Personal website</a></li>
            </ul>
        </div>
    </div>
    {%- else -%}
    <div class="thumbnail" style="width:160px">
        <img src="/img/oc/default.png" style="object-fit: cover; height:160px; width:100%;">
        <div class="caption">      
            <p><b>{{- speaker.name -}}</b></p>
            <p>{{- speaker.organisation -}}</p>
            <em>Speaker information coming soon.</em>
        </div>        
    </div>
    {%- endif -%}
{% endfor %}    
</div>
