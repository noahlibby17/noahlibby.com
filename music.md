---
layout: posts
title: Music
permalink: /music/
author_profile: true
---

{% for page in site.pages %}
  {% if page.url == '/music/allido' %}
[{{ page.title }}]({{ page.url }})
  {% endif %}
{% endfor %}
