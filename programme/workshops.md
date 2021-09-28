---
layout: default
---

# Accepted Workshops

####Monday 1st of November

{%for workshop in site.workshops%}

{%if workshop.date = Monday%}

 - [{{workshop.title}}]({{workshop.url}})
{%endif%}{%endfor%}

####Friday 5th of November

{%for workshop in site.workshops%}

{%if workshop.date = Friday%}

 - [{{workshop.title}}]({{workshop.url}})
   {%endif%}{%endfor%}
