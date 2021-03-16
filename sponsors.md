---
# DO NOT MANUALLY EDIT THIS FILE.
# TO EDIT SPONSORS, USE `_data/sponsors.yml`
layout: default
---

# Sponsors

{% for tier in site.data.sponsors.tiers %}
## {{ tier.level }}
{% for sponsor in tier.sponsors %}
<a href="{{- sponsor.url -}}">
    <img alt="{{- sponsor.name -}}" src="{{- sponsor.img_url -}}" style="max-height:120px">
</a>
{% endfor %}
{% endfor %}