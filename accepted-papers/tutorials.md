---
layout: default
---

{% assign days = "" | split: "," %}
{% for i in (0..6) %}
    {% for tutorial in site.data.accepted-papers.tutorials %}
        {% if tutorial.date_order == i %}
            {% if days contains i %}{% else %}
            {% assign days = days | push: i %}
            {% endif %}
        {% endif %}
    {% endfor %}
{% endfor %}

# Tutorials

{% for day in days %}
## {% include day_of_week.html day=day %}
<ul>
{% for tutorial in site.data.accepted-papers.tutorials %}
{% if tutorial.date_order == day %}
<li>{% include paper.html paper=tutorial %}</li>
{% endif %}
{% endfor %}
</ul>
{% endfor %}


