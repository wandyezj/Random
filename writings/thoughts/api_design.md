# API Design

## Abstract

What is an Application Programming Interface (API)?

> An API is "a set of clearly defined methods of communication among various components" per [Wikipedia's article on Application Programming Interface][API Wikipedia].

> "An  API  is  the  interface  to  implemented  functionality  that  developers  can  access  to  perform various  tasks." per [What makes APIs Hard to learn? Answers from Developers][What makes APIs Hard to learn? Answers from Developers]

What is the purpose of an API?

> The purpose of an API is to make knowledge accessible.

What is knowledge in the context of an API?

> Knowledge in the context of an API is functionality to perform programming tasks.

What is accessible knowledge?

> Knowledge that is accessible is discoverable and usable by others with minimal effort.

What is a reasonable process to follow to develop an API?

What are some considerations when developing an API?

> This paper will attempt to answer that question.

## Paper Structure



Like all software an API is constantly in development

The paper is structured

Links to [referenced papers](#references) with summaries of their contents are at the end of the paper


## Importance

A well designed API can significantly reduce the life-cycle cost of software. A Poorly designed API can significantly increase the life-cycle cost of software.

Reasons Why:

API Surface

Assume Functionality already exists


## Purpose, Principals, Patterns

## Purpose


## Context

How is the knowledge to be communicated defined?

## Documentation

## Process for Fulfilling Purpose

tricky since party an API is a form of communication.


## References

### API Definition

[API Wikipedia]: https://en.wikipedia.org/wiki/Application_programming_interface
[API Wikipedia][API Wikipedia]

```
an application programming interface (API) is a set of subroutine definitions, communication protocols, and tools for building software. In general terms, it is a set of clearly defined methods of communication among various components. A good API makes it easier to develop a computer program by providing all the building blocks, which are then put together by the programmer.
```

### API Importance

[API Design and Why it matters]: https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/32713.pdf "API Design and Why it matters"
[API Design and Why it matters][API Design and Why it matters]

* Successful Public APIs capture customers
* Bad APIs result in support calls
* Public APIs are forever
* Thinking in terms of APIs improves code quality

[API Design Matters]: https://queue.acm.org/detail.cfm?id=1255422 "API Design Matters"
[API Design Matters][API Design Matters]

* Poor APIs are difficult to program with and often require additional code to be written
* poor APIs are harder to understand and more difficult to work with than good ones
* Poor APIs often require not only extra code, but also more complex code that provides more places where bugs can hide

* Poor APIs Increase the cost to develop software
    * Time to Understand
    * Time to Write
    * Time to test
    * Time to fix bugs

* Poor APIs cost everyone time.

[The Little Manual of API Design]: http://people.mpi-inf.mpg.de/~jblanche/api-design.pdf "The Little Manual of API Design"

### API Solution

[The World and The Machine]: https://courses.cs.washington.edu/courses/csep503/19wi/schedule/papers/TheWorldAndTheMachine.pdf "The World and The Machine"
[The World and The Machine][The World and The Machine]

### API Usability

[Measuring API Usability]: http://www.drdobbs.com/windows/measuring-api-usability/184405654 "Measuring API Usability"
[Measuring API Usability][Measuring API Usability]

* Scenario based approach
* Evaluate actual users attempting to accomplish tasks

[What makes APIs Hard to learn? Answers from Developers]: https://www.cs.mcgill.ca/~martin/papers/software2009a.pdf "What makes APIs Hard to learn? Answers from Developers"
[What makes APIs Hard to learn? Answers from Developers][What makes APIs Hard to learn? Answers from Developers]

* APIs Structure
* API learning resources - most important for learning an API
    * Documentation
    * Code Examples
    * Experimentation
    * Articles
    "efforts to improve the us-ability of an API’s structure need to be complemented  by  efforts  to  improve  the  resources  available to learn them"
* API Documentation Must
    * include good examples
    * be complete
    * support many complex usage scenarios
    * be conveniently organized
    * include relevant design elements
* Understanding Design Aspects and Rationale
    * Understanding APIs high level design
* Working with Code Examples
    * snippets - basic API functionality
    * tutorials - complete application
    * applications - samples, and open source projects

[An Empirical Study of API Usability]: https://bugcounting.net/pubs/esem13.pdf "An Empirical Study of API Usability"
[An Empirical Study of API Usability][An Empirical Study of API Usability]

### API Model

[The Design of Everyday Things by Don Norman]: http://www.nixdell.com/classes/HCI-and-Design-Spring-2017/The-Design-of-Everyday-Things-Revised-and-Expanded-Edition.pdf "The Design of Everyday Things by Don Norman"
[The Design of Everyday Things by Don Norman][The Design of Everyday Things by Don Norman]

[Instruction Set Architectures]: https://en.wikipedia.org/wiki/Instruction_set_architecture "Instruction Set Architectures"
[Instruction Set Architectures][Instruction Set Architectures]

[Hypertext Transfer Protocol]: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol "Hypertext Transfer Protocol"
[Hypertext Transfer Protocol][Hypertext Transfer Protocol]

[A Relation Model of Data form Large Shared Data Banks]: https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf "A Relation Model of Data form Large Shared Data Banks - E. F. Codd"
[A Relation Model of Data form Large Shared Data Banks][A Relation Model of Data form Large Shared Data Banks]

[An Introduction to Software Architecture]: https://courses.cs.washington.edu/courses/csep503/19wi/schedule/papers/IntroSA.pdf "An Introduction to Software Architecture"
[An Introduction to Software Architecture][An Introduction to Software Architecture]

### API Structure

[C++ Core Guidelines]: http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines "C++ Core Guidelines"
[C++ Core Guidelines][C++ Core Guidelines]

[JavaScript Style Guide and Coding Conventions]: https://www.w3schools.com/js/js_conventions.asp "JavaScript Style Guide and Coding Conventions"
[JavaScript Style Guide and Coding Conventions][JavaScript Style Guide and Coding Conventions]

### API Behavior

[Software Testing: A Research Travelogue (2000–2014)]: https://courses.cs.washington.edu/courses/csep503/19wi/schedule/papers/SoftwareTestingTravelogue.pdf "Software Testing: A Research Travelogue (2000–2014)"
[Software Testing: A Research Travelogue (2000–2014)][Software Testing: A Research Travelogue (2000–2014)]

[An Overview of Formal Methods Tools and Techniques]: https://courses.cs.washington.edu/courses/csep503/19wi/schedule/papers/AnOverviewOfFormalMethodsToolsAndTechniques.pdf "An Overview of Formal Methods Tools and Techniques"
[An Overview of Formal Methods Tools and Techniques][An Overview of Formal Methods Tools and Techniques]

### API Review

[API Design Reviews at Scale]: https://storage.googleapis.com/pub-tools-public-publication-data/pdf/45294.pdf "API Design Reviews at Scale"
[API Design Reviews at Scale][API Design Reviews at Scale]


### Other

[How to write a technical paper]: https://homes.cs.washington.edu/~mernst/advice/write-technical-paper.html "How to write a technical paper"
[How to write a technical paper][How to write a technical paper]

[Robust De-anonymization of Large Datasets]:https://courses.cs.washington.edu/courses/csep503/19wi/schedule/papers/deanonymization.pdf "Robust De-anonymization of Large Datasets"
[Robust De-anonymization of Large Datasets][Robust De-anonymization of Large Datasets]

