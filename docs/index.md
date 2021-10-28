---
layout: page
title: Home
nav_order: 1
---

# **S**ocial **S**cience **C**omputing **U**nit - **B**udapest

> A unit dedicated to aiding the production of high quality, reproducible and extendable social science research.

Our goal is to build and maintain a diverse portfolio of complex, mostly large-scale datasets, we can use to create:

- reproducible and extendable multidisciplinary research
- scalable computational methods that generalize well for problems dealing with data concerning human behavior, social networks, geolocation, organizational structure and similar useful topics
- clear rules, procedures and infrastructure for data sharing and access
- connections between researchers of different fields who might benefit from similar data sources or computational approaches
- systems that automatically update datasets and research projects based on them

These datasets are intended to be created based on researcher requests by either collecting and organizing publicly available data, or processing purchased data.

Here is what we have been up to recently:

{% for topic in site.topics %}
## {{ topic.plural }}

{% include release_list.html topic=topic.topic_id limit=3 write_repo=true%}

{% endfor %}
