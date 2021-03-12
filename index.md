---
layout: homepage
---

Put some information here!

## Latest News

<div class="news flex one three-1000">
<div class="two-third-1000">
{% for post in site.posts limit:3 %}
<a href="{{ post.url }}"><h3>{{ post.title }}</h3></a>
<small>{{ post.date | date_to_long_string }}</small>
<p>{{ post.excerpt }}</p>
{% endfor %}
</div>
</div>

<a href="/posts/">News archive &rarr;</a>