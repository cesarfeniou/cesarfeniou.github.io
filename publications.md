---
layout: default
title: Publications
permalink: /publications/
---

<div class="publications-header">
  <h1 class="page-title">Publications</h1>
  <p class="intro-meta">
    You can also find my work on 
    <a href="https://scholar.google.com/citations?user=atHK9rYAAAAJ&hl" target="_blank" class="scholar-link">
      Google Scholar <i class="fas fa-external-link-alt"></i>
    </a>
  </p>
</div>

<div class="content publications-list">
  {% bibliography --group_by none --sort_by year --order descending %}
</div>
