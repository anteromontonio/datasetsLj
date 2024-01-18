---
layout: default
title: Home
---

<!-- <div class="posts">
  {% for post in paginator.posts %}
  <div class="post">
    <h1 class="post-title">
      <a href="{{ post.url | absolute_url }}">
        {{ post.title }}
      </a>
    </h1>

    <span class="post-date">{{ post.date | date_to_string }}</span>

    {{ post.content }}
  </div>
  {% endfor %}
</div>

<div class="pagination">
  {% if paginator.next_page %}
    <a class="pagination-item older" href="{{ paginator.next_page_path | absolute_url }}">Older</a>
  {% else %}
    <span class="pagination-item older">Older</span>
  {% endif %}
  {% if paginator.previous_page %}
    {% if paginator.page == 2 %}
      <a class="pagination-item newer" href="{{ '/' | absolute_url }}">Newer</a>
    {% else %}
      <a class="pagination-item newer" href="{{ paginator.previous_page_path | absolute_url }}">Newer</a>
    {% endif %}
  {% else %}
    <span class="pagination-item newer">Newer</span>
  {% endif %}
</div> -->


<!-- <p class="message">
  Hey there! This page is included as an example. Feel free to customize it for your own use upon downloading. Carry on!
</p> -->

This is a website designed and maintained by some people doing Discrete Math in Ljubljana, Slovenia

Ideally, we would host some datasets nicelly presented here, currently we have:

{% for post in site.datasets %}
 * [{{ post.title }}]({{ post.url }})
{% endfor %}




<!-- ## This would be a title H2


A table:

|header1|Header2|
|-------|-------|
|An entry|with something|
|Another one|With something else| -->
