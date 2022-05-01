---
layout: page
title: Projects
nav_order: 5
---

{% for project in site.projects %}
## {{ project.name }}

*[here](https://github.com/{{site.github_username}}/{{project.repo_name}}) at metadata version {{project.last_version}} last tagged {{project.last_published}}*

<!-- <div class="github-card" data-github="{{site.github_username}}/{{project.repo_name}}" data-width="500" data-height="" data-theme="default"></div> -->

{% endfor %}
