--- 
layout: page
title: Cubic vertex-transitive graphs
---



### Tables 
<ol>
{% for post in site.tables %}
  {% if post.dataset == 'cvtGraphs' %}
 <li> A <a href= "{{ site.url }}{{ post.url | relative_url }}" > table </a> containing the entries from {{ post.first_entry }} to {{ post.last_entry }} </li>
{% endif %}{% endfor %} 
 </ol>


### Resources

[Cubic vertex-transitive graph library](https://github.com/rhysje00/cvt) (in 
development) -- A GAP package containing all cubic vertex-transitive graphs on
up to 1280 vertices.