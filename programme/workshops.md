# Workshops Programme

For more information about a workshop, please click on a relevant link below.

{% assign days = "" | split: "," %}
{% for i in (0..6) %}
    {% for workshop in site.workshops %}
        {% if workshop.date_order == i or workshop.date_order contains i %}
            {% if days contains i %}{% else %}
            {% assign days = days | push: i %}
            {% endif %}
        {% endif %}
    {% endfor %}
{% endfor %}

{% for day in days %}
## {% include day_of_week.html day=day %}
{% for workshop in site.workshops %}
{% if workshop.date_order == day or workshop.date_order contains day %}
 - [{{workshop.title}}]({{workshop.url}})
{% endif %}
{% endfor %}
{% endfor %}




