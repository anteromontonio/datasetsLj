---
layout: page
title: Chiral Maps
---


Some description about the dataset

### Tables
<ol>
{% for post in site.tables %}
    {% if post.dataset == 'chirMaps' %}
        <li> <a href= "{{ site.url }}{{ post.url }}" > A table </a> </li>
    {% endif %}
{% endfor%}
</ol>

### Resources
- [README file](https://users.fmf.uni-lj.si/potocnik/RotaryMaps/Census-RotaryMaps-README.txt) with documentation for MAGMA
