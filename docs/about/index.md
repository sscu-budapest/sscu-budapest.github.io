---
layout: page
title: About
nav_order: 2
has_children: true
seo:
  name: 
    - SSCUB
    - Social Science Computing Unit Budapest
    - sscu-budapest
  type: Organization

---

# **S**ocial **S**cience **C**omputing **U**nit - **B**udapest

## Founding purpose

Aid the production of valuable social science research involving complex data processing, on large and interconnected datasets.

---

Our goal is to build and maintain a diverse catalog of complex, mostly large-scale datasets, we can use to create:

- reproducible and extendable multidisciplinary research
- scalable computational methods that generalize well for problems dealing with data concerning human behavior, social networks, geolocation, organizational structure and similar useful topics
- clear rules, procedures and infrastructure for data sharing and access
- connections between researchers of different fields who might benefit from similar data sources or computational approaches
- systems that automatically update datasets and research projects based on them

These datasets are intended to be created based on researcher requests by either collecting and organizing publicly available data, or processing purchased data.


## Challenges

Most challenges arise from the **complexity** that the intertwined chains of operations applied to the data present, with the need to take into account certain factors that are usually not present while conducting social science research. Als, from the **access management** issue where sensitive information needs to be processed in a published and reproducible way.

Most common resulting issues:

- Difficulty of presentation
- Reuse
  - reproduction
  - extension
- Redundant, repeated work
- Possible cascading errors

Many of the main issues are expanded in [this](https://scholar.harvard.edu/files/gking/files/1060.full_.pdf) article

## Approach

### Operational Practice Borrowed from Software Engineering

- Adopt carefully selected [tooling](/tooling) designed for large scale, complex data related software projects.
- Public and searchable [task board](https://github.com/orgs/sscu-budapest/projects/2) for transparency and cooperation.
- Clear set of guiding [principles](/principles) like [FAIR](https://www.nature.com/articles/sdata201618.pdf) and [JDDCP](https://www.force11.org/datacitationprinciples) that can be cited during task priorization and other decision making.

### Openness

> All reports are open, all software is free and open-source, all data has a publicly available version


## Output

### Datasets

Self hosted datasets strictly adhering to an internally developed template, maintained and updated while involved in projects, fully contained in a git repository stored on github.

- contains **metadata**, **storage configuration** and description of **subsets**
- all datasets have at least one open and publicly available subset
  - this can be scrambled, anonymized, use random samples, anything
  - needs to be able to be used by any project using the dataset
- subsets are created using code available with the dataset
- only contain data from one source
  - merging different datasets fro different sources happens at the project level


### Research Projects

- all results are reproducible with one line of code
  - dataset subsets are interchangeable with a simple configuration modification
- full pipeline is visualized and documented


### Research Software

Open source software that is used across many projects and datasets, deemed worthy to be abstracted away and not found in other open source options.

- tested
- documented
- quality controlled
- open source
