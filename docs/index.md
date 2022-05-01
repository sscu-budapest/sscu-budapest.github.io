---
layout: page
title: Home
nav_order: 1
---

# **S**ocial **S**cience **C**omputing **U**nit - **B**udapest

A unit dedicated to aiding the production of high quality, reproducible and extendable social science research. We intend to make use of and extend open-source [tools](/tooling) that have matured and gained popularity mainly in commercial data analysis and data science uses.

---

Here is what we are doing:

## Providing a Platform for Exploration

We created a [Data Exploration Catalog](https://sscu-budapest.github.io/explorer/) prototype, where we publish datasets, present some basic analysis and possible avenues of research. The datasets in the exploration catalog can be subsets of larger sets or even intermediate output steps of research projects that researchers can freely download and test ideas on. Most of them update periodically. If an idea explored on a smaller subset looks promising, but the complexity or the scale of the full dataset requires it, we can assist in implementing a solution to see the results on the full set.

## Engineering Reproducible Research

Formalized, machine actionable, pipelines where all intermediate steps can be checked out and reused with minimal effort and without replicating code. A list of these can be found in the [projects](/projects) page

## Developing Research Software

A tested, documented main library that handles most of the above:

[![Documentation Status](https://readthedocs.org/projects/datazimmer/badge/?version=latest)](https://datazimmer.readthedocs.io/en/latest)
[![codeclimate](https://img.shields.io/codeclimate/maintainability/sscu-budapest/datazimmer.svg)](https://codeclimate.com/github/sscu-budapest/datazimmer)
[![codecov](https://img.shields.io/codecov/c/github/sscu-budapest/datazimmer)](https://codecov.io/gh/sscu-budapest/datazimmer)
[![pypi](https://img.shields.io/pypi/v/datazimmer.svg)](https://pypi.org/project/datazimmer/)
<div class="github-card" data-github="{{site.github_username}}/datazimmer" data-width="500" data-height="" data-theme="default"></div>

Contributions to closely or loosely related open source projects:

{% for contrib in site.contributions %}
- [{{contrib.name}}]({{contrib.link}}){% for pers in contrib.latest %}
  - [{{pers.name}}]() ({{pers.last}}){% endfor %}
{% endfor %}
