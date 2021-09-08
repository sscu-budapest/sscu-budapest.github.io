---
layout: page
title: Home
nav_order: 1
---

# **S**ocial **S**cience **C**omputing **U**nit - **B**udapest

> A unit dedicated to aiding the production of high quality, reproducible and extendable social science research.

Here is what we have been up to recently:

{% for topic in site.topics %}
## {{ topic.plural }}

{% include release_list.html topic=topic.topic_id limit=3 write_repo=true%}

{% endfor %}
