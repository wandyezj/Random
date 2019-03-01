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


A well designed API can significantly reduce the life-cycle cost of software. A Poorly designed API can significantly increase the life-cycle cost of software.

Reasons Why:

API Surface

Assume Functionality already exists

## Paper Structure

An Application Programming Interface (API) is ultimately a way to access functionality. One consideration of accessing functionality is ease of use: being able to quickly discover, understand, and apply the provided functionality. This paper will examine considerations for designing an API with ease of use in mind.

This paper will look at ease of use in four API aspects:

* [Model](#model),
* [Behavior](#behavior),
* [Structure](#structure), and,
* [Documentation](#documentation).

Each API aspect will explore its __purpose__, __principals__, and __patterns__ related to ease of use:

* __purpose__ is what it can contribute towards ease of use.
* __principals__ are intended to give high level direction towards design considerations.
* __patterns__ are derived from principals and are intended to give specific design guidance.


The end of the paper is a [reference section](#reference) that summarizes papers that pertain to ease of use.

### Personal Reference Philosophy

* References are descriptive links to the item in the reference section.
* External references are available via hyperlink for easy access.
* The Reference section summarizes the references to more easily understand key takeaways.

## Aspects

### Model

The model of an API is it's underlying paradigm. The model consists of both a __technical model__ and __mental model__. T

The __Technical Model__ is how the API is implemented and imposes constraints on design. In general the __Technical Model__ is usually a well known paradigm.

Some well known __Technical Models__ include:

* [Instruction Set Architectures](#Instruction-Set-Architectures) such as x86, AMD64, and ARM
* [Relational Model](#Relational-Algebra-Model) that backs most modern databases.
* [Hypertext Transfer Protocol](#Hypertext-Transfer-Protocol)
* Language Models: C, C++, JavaScript, TypeScript, Block programming etc...
    * Languages generally provide specific means to accomplish various programming tasks and generally come with a standard set of conventions.

The __Technical Model__ provides the foundation for which an API is based and comes with a certain set of expectations about how features in the model are used.

The __Mental Model__ is the users map of what that API represent and how that API pieces fit together to accomplish tasks. See [The Design of Everyday Things by Don Norman](The-Design-of-Everyday-Things-by-Don-Norman) chapter 1 for a good explanation of mental models.

#### Model Purpose

#### Model Principals

#### Model Patterns


### Behavior

What happens when an error occurs?

#### Behavior Purpose

#### Behavior Principals

#### Behavior Patterns


### Structure

#### Structure Purpose

#### Structure Principals

#### Structure Patterns

### Documentation

Making sure it works well and is accessible from a development environment

How the programmer types out an action

Documentation can exist on multiple levels:

* Mental Model
* Specific Calls
* Parameters
* Performance Limitations
* Interactions between APIs

#### Documentation Purpose

#### Documentation Principals

#### Documentation Patterns

* Paradigm Documentation
* Examples
* Applications
* Tutorials

## Conclusion

## Content

How is the knowledge to be communicated defined?


## Reference

### Teaching

[McKeachie's Teaching Tips: Strategies, Research, and Theory for College and University Teachers]: https://www.amazon.com/McKeachies-Teaching-Tips-Wilbert-McKeachie/dp/1133936792



### API Definition

[API Wikipedia]: https://en.wikipedia.org/wiki/Application_programming_interface
[API Wikipedia][API Wikipedia]

```text
an application programming interface (API) is a set of subroutine definitions, communication protocols, and tools for building software. In general terms, it is a set of clearly defined methods of communication among various components. A good API makes it easier to develop a computer program by providing all the building blocks, which are then put together by the programmer.
```

### API Importance

#### API Design and Why it matters
[API Design and Why it matters]: https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/32713.pdf "API Design and Why it matters"
[API Design and Why it matters][API Design and Why it matters]

* Successful Public APIs capture customers
* Bad APIs result in support calls
* Public APIs are forever
* Thinking in terms of APIs improves code quality

#### API Design Matters
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

#### The World and The Machine
[The World and The Machine]: https://courses.cs.washington.edu/courses/csep503/19wi/schedule/papers/TheWorldAndTheMachine.pdf "The World and The Machine"
[The World and The Machine][The World and The Machine]

### API Usability

#### Measuring API Usability
[Measuring API Usability]: http://www.drdobbs.com/windows/measuring-api-usability/184405654 "Measuring API Usability"
[Measuring API Usability][Measuring API Usability]

* Scenario based approach
* Evaluate actual users attempting to accomplish tasks

#### What makes APIs Hard to learn
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

#### An Empirical Study of API Usability

[An Empirical Study of API Usability]: https://bugcounting.net/pubs/esem13.pdf "An Empirical Study of API Usability"
[An Empirical Study of API Usability][An Empirical Study of API Usability]

#### Intelligent Code Completion
[Intelligent Code Completion]: https://en.wikipedia.org/wiki/Intelligent_code_completion
[Intelligent Code Completion][Intelligent Code Completion]

#### The Design of Everyday Things by Don Norman
[The Design of Everyday Things by Don Norman]: http://www.nixdell.com/classes/HCI-and-Design-Spring-2017/The-Design-of-Everyday-Things-Revised-and-Expanded-Edition.pdf "The Design of Everyday Things by Don Norman"
[The Design of Everyday Things by Don Norman][The Design of Everyday Things by Don Norman]

* The idea of a mental model distinct from the underlying technical

#### Instruction Set Architectures


[Instruction Set Architectures]: https://en.wikipedia.org/wiki/Instruction_set_architecture "Instruction Set Architectures"
[Instruction Set Architectures][Instruction Set Architectures]

* communicate with the CPU
* often have very specific behaviors and complex interactions
* many features

#### Hypertext Transfer Protocol
[Hypertext Transfer Protocol]: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol "Hypertext Transfer Protocol"
[Hypertext Transfer Protocol][Hypertext Transfer Protocol]

#### Relational Model
[A Relation Model of Data form Large Shared Data Banks]: https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf "A Relation Model of Data form Large Shared Data Banks - E. F. Codd"
[A Relation Model of Data form Large Shared Data Banks][A Relation Model of Data form Large Shared Data Banks]

* Presents a Technical Model of Relational Algebra for use in querying a database.

#### An Introduction to Software Architecture
[An Introduction to Software Architecture]: https://courses.cs.washington.edu/courses/csep503/19wi/schedule/papers/IntroSA.pdf "An Introduction to Software Architecture"
[An Introduction to Software Architecture][An Introduction to Software Architecture]

```text
it is important to be able to recognize common paradigms so that high-level relationships among systems can be understood
```

* Common patterns aid understanding
* Understanding high level relationships is important to understand the system as a whole.

Abstract Data Types

* software structure
* specifications
* language issues (modules, scope, types)
* invariant data structures
* information hiding

Architectural Styles

* Pipes and Filters
* Object Oriented
* Event Based
* Layered
* Repositories
* Interpreter
* Heterogenous


### API Structure

#### C++ Core Guidelines
[C++ Core Guidelines]: http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines "C++ Core Guidelines"
[C++ Core Guidelines][C++ Core Guidelines]

* Conventions to follow for C++ code

Philosophy

* Express ideas directly in code
* Express intent
* type safe
* compile time check then run time check
* don't waste time or space
* prefer immutable data to mutable data
* encapsulate messy constructs
* use supporting tools as appropriate

#### JavaScript Style Guide and Coding Conventions
[JavaScript Style Guide and Coding Conventions]: https://www.w3schools.com/js/js_conventions.asp "JavaScript Style Guide and Coding Conventions"
[JavaScript Style Guide and Coding Conventions][JavaScript Style Guide and Coding Conventions]

* improves code readability
* improve maintenance

* variable names
* spaces
* indentation
* naming conventions
* initialize variables
* be aware of automatic type conversion
* be aware of defaults


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

