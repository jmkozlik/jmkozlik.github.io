---
layout: default
title: Notes
permalink: /writing/
description: "Technical notes by Jonathan Kozlik."
---

<article class="page">
  <h1>Notes</h1>
  <p>Occasional technical notes, experiment reports, and things I want to remember.</p>

  {% if site.posts.size > 0 %}
  <ol class="note-list note-list-full">
    {% for post in site.posts %}
    <li>
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y-%m-%d" }}</time>
      <div>
        <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
        {% if post.summary and post.summary != empty %}
        <p>{{ post.summary }}</p>
        {% else %}
        <p>{{ post.excerpt | strip_html | normalize_whitespace | truncatewords: 32 }}</p>
        {% endif %}
      </div>
    </li>
    {% endfor %}
  </ol>
  {% else %}
  <p class="empty">No notes published yet.</p>
  {% endif %}
</article>
