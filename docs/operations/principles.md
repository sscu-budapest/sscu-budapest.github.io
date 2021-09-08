---
layout: page
title: Principles
permalink: /principles/
parent: Operations
nav_order: 3
---
# Sientific Data Management

## FAIR

[The FAIR Guiding Principles for scientific data management and stewardship](https://www.nature.com/articles/sdata201618.pdf)

Aim for machines to automatically find and use the data,  the principles apply not only to data, but also to the algorithms, tools, and workflows that led to that data: all scholarly digital research objects

### To be Findable
- F1. (meta)data are assigned a globally unique and persistent identifier
- F2. data are described with rich metadata (defined by R1)
- F3. metadata clearly and explicitly include the identifier of the data it describes
- F4. (meta)data are registered or indexed in a searchable resource

### To be Accessible
- A1. (meta)data are retrievable by their identifier using a standardized communications protocol
  - A1.1 the protocol is open, free, and universally implementable
  - A1.2the protocol allows for an authentication and authorization procedure, where necessary
- A2. metadata are accessible, even when the data are no longer available

### To be Interoperable
- I1. (meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation
- I2. (meta)data use vocabularies that follow FAIR principles
- I3. (meta)data include qualified references to other (meta)data

### To be Reusable
- R1. meta(data) are richly described with a plurality of accurate and relevant attributes
  - R1.1. (meta)data are released with a clear and accessible data usage license
  - R1.2. (meta)data are associated with detailed provenance
  - R1.3. (meta)data meet domain-relevant community standards


### Machine Actionable

when faced with a digital object never encountered before
- identify the type of object (with respect to both structure and intent)
- determine if it is useful within the context of the agent’s current task by interrogating metadata and/or data elements
- determine if it is usable, with respect to license, consent, or other accessibility oruse constraints
- take appropriate action, in much the same manner that a human would

two contexts:
- contextual metadata surrounding a digital object ('what is it?')
- content of the digital object itself ('how do I process it/integrate it?')


### Examples 

- [Dataverse](https://dataverse.org/)
  - e.g. [Harvard](https://dataverse.harvard.edu/)
- [FAIRDOM](https://fair-dom.org/about-fairdom/)
  - Systems  Biology
- [ISA](https://isa-tools.org/)
  - experiments and life sciences [github](https://github.com/ISA-tools)
- wwPDB, UniProt
  - protein and nucleic acids


## JDDCP

> [Joint Declaration of Data Citation Principles](https://www.force11.org/datacitationprinciples)

1. Importance
  - Data should be considered legitimate, citable products of research. Data citations should be accorded the same importance in the scholarly record as citations of other research objects, such as publications[1].
2. Credit and Attribution
  - Data citations should facilitate giving scholarly credit and normative and legal attribution to all contributors to the data, recognizing that a single style or mechanism of attribution may not be applicable to all data[2].
3. Evidence
  - In scholarly literature, whenever and wherever a claim relies upon data, the corresponding data should be cited[3].
4. Unique Identification
  - A data citation should include a persistent method for identification that is machine actionable, globally unique, and widely used by a community[4].
5. Access
  - Data citations should facilitate access to the data themselves and to such associated metadata, documentation, code, and other materials, as are necessary for both humans and machines to make informed use of the referenced data[5].
6. Persistence
  - Unique identifiers, and metadata describing the data, and its disposition, should persist -- even beyond the lifespan of the data they describe[6].
7. Specificity and Verifiability
  - Data citations should facilitate identification of, access to, and verification of the specific data that support a claim. Citations or citation metadata should include information about provenance and fixity sufficient to facilitate verifying that the specific timeslice, version and/or granular portion of data retrieved subsequently is the same as was originally cited[7].
8. Interoperability and Flexibility
  - Data citation methods should be sufficiently flexible to accommodate the variant practices among communities, but should not differ so much that they compromise interoperability of data citation practices across communities[8].

