--- 
layout: page
title: Chiral maps up to 6000 edges
---
This dataset contains the chiral maps up to 6000 edges, or equivalently those whose automorphism group is of order at most 12 000. 
Each entry of the dataset is labelled by an identifier of the form CM\[E,i\] where E denotes the number of edges of the map and i indicates that the entry is the i-th map with such number of edges.

### Tables 
<ol>
{% for post in site.tables %}
  {% if post.dataset == 'chiralMaps6kE' %}
 <li> A <a href= "{{ site.url }}{{ post.url | relative_url}}" > table </a> containing the entries from {{ post.first_entry }} to {{ post.last_entry }} </li>
{% endif %}{% endfor %} 
 </ol>


<!-- ### Resources -->