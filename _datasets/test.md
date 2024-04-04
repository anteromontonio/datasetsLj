--- 
 layout: page
 title: Testing dataset
 permalink: /test/
---


This dataset contains (at least) the following information for every entry:
- **ID**: ID
- **genus**: Genus of the underlying surface
- **p**: Length of the face
- **q**: Valency
- **r**: Length of the Petrie polygon
- **solv**: Is the automorphism group solvable?
- **V**: Number of vertices
- **E**: Number of edges
- **F**: Number of faces
- **vMult**: Vertex multiplicity
- **fMult**: Face multiplicity
- **self**: The map is self-
- **Du**: Dual map
- **Mir**: Mirror (enantihomorphic) map
- **DuMir**: Dual of the mirror image
- **Zq*:Exp**: Z_q-Exponent?
- **Hj**: No idea
- **plt**: No idea
- **plh**: No idea
- **Sk**: Skeleton
- **PlhSk**: Some other kind of skeleton

### Resources
- You can download a csv file containing the data on this dataset [here]({{ site.url }}/csv/test.csv) 



### Tables 
<ol>
{% for post in site.tables %}
  {% if post.dataset == 'test' %}
 <li> <a href= "{{ site.url }}{{ post.url | relative_url }}" > Table </a> containing the entries from {{ post.first_entry }} to {{ post.last_entry }} </li>
{% endif %}{% endfor %} 
 </ol>

