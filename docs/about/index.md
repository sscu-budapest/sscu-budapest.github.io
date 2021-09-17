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

> Aid the production of valuable social science research involving complex data processing, on large and interconnected datasets.


## Challenges

Most challenges arise from the **complexity** that the intertwined chains of operations applied to the data present, with the need to take into account certain factors that are usually not present while conducting social science research. Als, from the **access management** issue where sensitive information needs to be processed in a published and reproducible way.

Most common resulting issues:

- Difficulty of presentation
- Reuse
  - reproduction
  - extension
- Redundant, repeated work
- Possible cascading errors


## Approach

### Operational Practice Borrowed from Software Engineering

- Adopt carefully selected [tooling](/tooling) designed for large scale, complex data related software projects.
- Public and searchable [task board](https://github.com/orgs/sscu-budapest/projects/1) for transparency and cooperation.
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
