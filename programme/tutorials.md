# Tutorials Programme

For more information about a tutorial, please click on a relevant link below.

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

{% for day in days %}
## {% include day_of_week.html day=day %}
{% for tutorial in site.tutorials %}
{% for accepted_tutorial in site.data.accepted-papers.tutorials %}
{% if tutorial.acm_id == accepted_tutorial.acm_id and accepted_tutorial.date_order == day or accepted_tutorial.date_order contains day %}
 - [{{accepted_tutorial.title}}]({{tutorial.url}})
{% endif %}
{% endfor %}
{% endfor %}
{% endfor %}




