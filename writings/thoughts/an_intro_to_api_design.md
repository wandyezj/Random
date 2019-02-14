# API Design and Software Quality

## Thesis

Application Programming Interfaces (APIs) are the chief method for programmers to interact with software. APIs design can have a substantial impact on software quality.

This paper will examine API design flaws that lead to undesireable outcomes and analyze what could have been done to prevent these flaws.

This paper will examine:

* the general components of an API
* specific case studies where flaws in API design lead to undesireable outcomes
* an API design process to reduce API design flaws

This paper attempts to understand the components of tha API, show that flaws in APIs Design can lead to undesireable outcomes, and proposes a high level API Design process to attempt to reduce API design flaws.



## API Components

Before examining specific cases where API design flaws lead to undesireable outcomes it is worth examining the components of an API to better understand where design flaws can occur.

To simplify the disucssion we will consider APIs to be composed of three components:

* [Model](#model)
* [Structure](#structure)
* [Behavior](#behavior)

### Model

The model of an API is it's underlying paradigm. The model consists of both a underlying __technical model__ as well as __mental model__ of the APIs meaning.

__Technical models__ are usually well documented interface models such as:

* [Instruction Set Architectures](https://en.wikipedia.org/wiki/Instruction_set_architecture) such as x86, AMD64, ARM 
* the [Relational Model][Relational Algebra Model] that backs most modern databases.
* [Hypertext Transfer Protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
* Language Models: C, C++, JavaScript, Block programming etc... Languages generally provide specific means to accomplish various programming tasks and generally come with a standard set of conventions.

How is the technical model decided?
    * Usually don't have a choice
    * Essentially the technical model is domain specific
    * we are looking for general rules that apply to all domains
    * The domain can influence the mental model of users since the come at the API with a certain mind set


__Mental models__ are the models that API users form in their head of how the API works. See [The Design of Everyday Things by Don Norman](http://www.nixdell.com/classes/HCI-and-Design-Spring-2017/The-Design-of-Everyday-Things-Revised-and-Expanded-Edition.pdf) for a full explanation of mental models. While Don Norman is generally describing interaction with physical objects the same concepts apply to APIs.

How is the API Mental model shaped?
What role does the mental model play in how the API is used?
    * if users can't for a clear mental model they can't figure out how to use the API
    * possibly use the API incorrectly

### Structure

The structure of an API is the specific naming and parameters of function names, classes, interfaces, etc. that are used to interact with the API. The structure of an API is generally heavily influenced by its technical model as well as the mental model the API is attempting to project. The structure of an API is also influenced by the other APIs around it which may conform to an overall Architectural model as discussed in [An Introduction to Software Architecture](https://courses.cs.washington.edu/courses/csep503/19wi/schedule/papers/IntroSA.pdf)

What are some conventions that structures follow?
    * Domain dependent
    * JavaScript conventions
    * naming coventions: see C++ standards

[C++ Core Guidelines]: http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines "C++ Core Guidelines"
    * There may be conventions specific to the domain, such as Windows APIs
[JavaScript Style Guide and Coding Conventions]: https://www.w3schools.com/js/js_conventions.asp "JavaScript Style Guide and Coding Conventions"

    * Style is important for APIs so users know what to expect

### Behavior

The behavior and an API is what the API specifically does, or the effect that the API produces under specific circumstances. In some circumstances the APIs behavior may choose to be undefined. For example the parallel programming API standard [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) defines some behavior as intentionally undefined to allow freedom of implementations while stil maintaining the overall standard.

What is good behavior?

## Case Studies

Now that we have examined the components of an API we may examine case studies where API design flaws lead to undesireable outcomes.

### C / C++ strcpy

The [strcpy](http://www.cplusplus.com/reference/cstring/strcpy/) function in C and C++ is a well known example of an API design flaw. The underlying technical model in C / C++ allows arrays memory to be accessed beyond what was allocated. The strcpy function offered a simple mental model it would copy the contents of one string into another. The flaw in the API was that it did not offer a means to check that it was not copying over beyond the memory allocated in the destination string. Doing the check requires that outside code check the length of the source string and the length of the destination buffer and verify that the destination had enough length for the source. Without this check there is the possibility that the strcpy function would write beyond the length of the destination buffer directly into program memory possibly corrupting other program memory contents, this type of misfunction is named [Buffer Overflow](https://en.wikipedia.org/wiki/Buffer_overflow). The simplicity of strcpy and the mental model if provided made it extreamly easy to forget to do this extra check outside of the function leading to many Buffer Overflow vulnerabilites from this API. Patching these vulnerabilities requires extreamly costly inspection of all code that could contain a strcpy function to ensure that it was being used correctly.

The flaw in the design is two fold: First the underlying technical model in C / C++ allowed behavior that is clearly generally undesireable. Second the mental model of strcpy did not prompt or warn users of the need to do an additional check. 

Various alternative API designs exist that could have prevented this flaw:

The model in C / C++ could have prevented writing off of the end of a buffer.

The C++ string class helps mitigate the need to guard against buffer overflow when manipulating strings by providing an API that stores the length of the buffer with the  

Some C / C++ compilers generate additional code to help prevent such issues such as [Control Flow Guard](https://docs.microsoft.com/en-us/windows/desktop/secbp/control-flow-guard). This helps relieve some of the mental burden on the programmer to fix such issues.

Linters can prompt programmers to use strcpy correctly and verify that the programmer checked that the destination has enough room for the source buffer.

Alternatively the API could have been designed in the first place to account for Buffer Overflow possibility in the model and prompt users to prevent such conditions by providing the length of the destination buffer as a future iteration of the API strcpy_s does.

The lesson is that an APIs structure aids the mental model programmers form and can help work around limitations in the technical model.



[Control Flow Guard]: https://docs.microsoft.com/en-us/windows/desktop/secbp/control-flow-guard

### NASA’s Mars Climate Orbiter - Spacecraft Metric to Imperial units

[NASA's Mars Climate Orbiter](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) mission failed partially due to poor API design at the cost of 327.6 million dollars.

The primary cause of failure was that the software library provided by a contractor specified different units than those assumed by the user of the library.

See below quotes from the wikipedia article:

```
computer software which produced output in non-SI units of pound-force seconds (lbf·s) instead of the SI units of newton-seconds (N·s) specified in the contract between NASA and Lockheed.
```

```
The primary cause of this discrepancy was that one piece of ground software supplied by Lockheed Martin produced results in a United States customary unit, contrary to its Software Interface Specification (SIS), while a second system, supplied by NASA, expected those results to be in SI units, in accordance with the SIS. Specifically, software that calculated the total impulse produced by thruster firings produced results in pound-force seconds. The trajectory calculation software then used these results – expected to be in newton seconds – to update the predicted position of the spacecraft.[16] Still, NASA does not place the responsibility on Lockheed for the mission loss; instead; various officials at NASA have stated that NASA itself was at fault for failing to make the appropriate checks and tests that would have caught the discrepancy
```

How could this happen? This seems like a flaw in the structure of the API provided.



 have specified in it's name and documentation the units that it




### Windows GetVersion - compatibility

The Windows [GetVersion API][GetVersion API] is an example where the API works as intended but the underlying mental model is flawed.

The GetVersion API was intended to get the Operating Systems version.

Developers ended up using the API as a shortcut to tie their application to a specific Operating System that they had verified their application on and would exit their application if a different Operating System version than expected were detected.

An additional structural problem with this API is the way that the version is returned as a single DWORD that contains both the Major and Minor version. Developers would then have to parse out the Major and Minor version from the DWORD. As you can imagine this is not a trivial task and many developers got it wrong and did not get their behaviro as expected.

This versioning API caused many Compatability issues for applications as new Operating System versions were released. New Operating Systems had higher versions which causes applications that would have worked perfectly well on newer Operating System versions to fail simply due to a version check.

Since so many critical applications broke due to the abuse and misues of this API this required that eventually the API be completely replaced with a shim that lies to applications about what the underlying Operating System version is so that these applications would work.



 tell what features were supported and would tie their applications to a specific operating system.

 so that developers could tell what features were supported by the OS.

Developers ended up using

s model was flawed as developers used the A


Developers ended up using the API as a shortcut, Not as intended, additionally the APIs structure was flawed where developer could easily misuse the returned version. This caused many compatability issues where software that was capable of running on newer versions of the Operationg System were unable to run due to the check. In order to keep applications working the API had to be shimmed, and essentially ended up a a liability instead of an asset.

[GetVersion API]: https://docs.microsoft.com/en-us/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getversion

## API design process

The process of API design is a knowledge capture exercise. The goal of the API Design process is to capture as much information as possible into the APIs specification and clearly communicate that information to the implementers and users of the API.

API Designs that are useful, intuitive, and testable can be time consuming to produce but the results are worth it.

What can be done to maximize the benefit of the design process?

The first thing that can be done to maximize the benefit of the design process is to think about an API as a standard to be applied to many situations. Many applications have similar needs or are made of of similar components there is no need to reinvent how to achieve an action.

### Standard API

An API should be thought of as a standard.

Where possible APIs should be made abstract enough to apply across applications to common scenarios so that the same API pattern can be directly taken to new areas with only implementation details changing.

Developers should only have to learn a pattern once for it to be widely applicable.

Allowing the same API structure allows all the thought that went into the: design, documentation, and tests to be taken to the new implementation. This frees developers to focus on the interesting specific implementation and to innovate in new areas. 

## The API Design Exercise

API design is an iterative process that should happen **before** implementation, constrained by implementation details.

Throughout the exercise the proposed design should be made available for review and iterated on as needed.

None of the design steps are do once, instead the design process goes between steps as needed. Changes in previous design steps will impact later steps.


1. [Scenarios](#scenarios)
1. [Shape](#shapes)
1. [Documentation](#documentation)
1. [Units](#units)
1. [Mocks](#mocks)
1. [Review](#review)


### Scenarios

First, API scenarios are defined: What should consumers of the API be able to do?

Scenarios should:

* define a real world use case where the API is immediately useful
* consider how to make the API general enough to apply to similar cases

It's best to create an API when there is a real world need that is immediately served by the API. As dicussed in [The World and The Machine](https://courses.cs.washington.edu/courses/csep503/19wi/schedule/papers/TheWorldAndTheMachine.pdf) the first step to specifically understand the problem that is to be solved and what the API contributes to solving the problem.

### Shape

Next, the API shape is defined: interfaces, classes, enums, methods, etc...

Ultimately the specific API shape is heavily influenced by the underlying model choosen for the API, architectural choices, and specific implementation language. 

Shape should:

* make intuitive sense to many people without extensive background or documentation

The goal of API shape is to clearly project a mental model to the consumer of the API as to what the API does and how to use it. 

### Documentation

Next, the the various shapes are documented.

Documentation should:

* cover the specific behavior of the API
* give examples of how the API is used

What data can the API expose? (Privacy)
Who can access the API? (Security)

### Units

Next, the documentation is turned into unit tests that would ideally exercise all aspects of the API as specified by the documentation, including error conditions.

As discussed in [An Overview of Formal Methods Tools and Techniques](https://courses.cs.washington.edu/courses/csep503/19wi/schedule/papers/AnOverviewOfFormalMethodsToolsAndTechniques.pdf) there are various formal methods for software verification. Ideally every API could and would be formally verified. Unfortunantly, there are severe limitations to current formal methods, especially when APIs can abstract complex interactions underneath and can be linked to hetrogenous systems that are difficult to formally verify. Another drawback to formal methods is that currently applying these techniques is extreamly costly and thus generally not feasible for most software development. Additionally, while formal methods may prove something mathmatically there is a difference between a mathmatical proof of software and software actually running on a real world system. Thus while verification can be a helpful tool its limitations mean that real world testing is still required.

As discussed in [Software Testing: A Research Travelogue (2000–2014)](https://courses.cs.washington.edu/courses/csep503/19wi/schedule/papers/SoftwareTestingTravelogue.pdf) there are many ways to test software. Software testing provides a different set of guarentees than formal methods. Testing does not prove that software behaves in all circumstances according to documentation. Testing can show that an API produces the correct behavior in specific cases giving some confidence that the API performs correctly in similar cases. Testing is generally significantly less costly to implement than formal software verification methods. 

The general software testing follows a standard of expected input and comparing actual output with expected output. Some output can be more difficult to test than others especially if it results in complex behavior dependent on an internal state.

The overall idea of writing the unit tests is to clearly explain what the APIs behavior looks like, and as a bonus potentially provide tests for actual implementation.

Units should:

* be specific
* easy to understand
* runnable tests
* cover common edge cases

What is the purpose of units?
    * ensure API performs as designed and documented
    * show specifically how API behaves

### Mocks

Next, the defined scenarios are mocked up with the API to show that the API meets the scenario requirements.

Mocks should:

* show that the API accomplishes the defined scenario
* show at a high level that the API interacts well with existing APIs

The idea of mocks is to give reviewers of the API an idea of how the API interacts with other APIs to solve the actual scenario. This is a test that the API actually serves the purpose it was designed for.

### Review

Throughout the process and at all phases the API should be available for review

APIs are always in progress

Review can happen in many ways:
* Feedback from users using a deployed API
* 


## API Operation

## API Retirement



## Conclusion

Analysis of where to prevent issues common causes




## Reference

[How to write a technical paper]: https://homes.cs.washington.edu/~mernst/advice/write-technical-paper.html "How to write a technical paper"

[Robust De-anonymization of Large Datasets][Robust De-anonymization of Large Datasets]
[Robust De-anonymization of Large Datasets]:https://courses.cs.washington.edu/courses/csep503/19wi/schedule/papers/deanonymization.pdf "Robust De-anonymization of Large Datasets"

[An Empirical Study of API Usability][An Empirical Study of API Usability]
[An Empirical Study of API Usability]: https://bugcounting.net/pubs/esem13.pdf "An Empirical Study of API Usability"

```
Finding  descriptive,  non-ambiguous  names  for  API  fea-tures is problematic given that programmers may be usedto different terminologies

Discovering  relations  between  API  types  (classes)  re-quires  significant  effort;  simple  designs  are  beneficial,especially to less experienced programmers.

Accurate  and  complete  documentation  is  a  crucial  issuefor API usability; all the major usability flaws discoveredin our study trace back to unsatisfactory documentation.

Flexibility is a double-edged sword in API design: expe-rienced programmers can take advantage of it, but it mayconfuse those with less practice.
```

Concept of Negative Usability Tokens

[How to Design A good API and why it matters][How to Design A good API and why it matters]
[How to Design A good API and why it matters]:https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/32713.pdf

[What makes APIs Hard to learn? Answers from Developers][What makes APIs Hard to learn? Answers from Developers]
[What makes APIs Hard to learn? Answers from Developers]: https://www.cs.mcgill.ca/~martin/papers/software2009a.pdf "What makes APIs Hard to learn? Answers from Developers"

Essentially documentation is important, and some specifics about what make good examples.

```
Namely, to mitigate obstacles, API docu-mentation must 
■ include good examples, 
■ be complete, 
■ support many complex usage scenarios, 
■ be conveniently organized, and 
■ include relevant design elements.
```

Code Examples:

```
Among  these,  the  most  prevalent  frustration was  that  snippets didn’t  provide  any  support  for thinking about “how to put things together:”
```

[API Design Reviews at Scale][API Design Reviews at Scale]
[API Design Reviews at Scale]: https://storage.googleapis.com/pub-tools-public-publication-data/pdf/45294.pdf "API Design Reviews at Scale"

Focuses on the review process.

Key Takeaways:

* Fast feedback
* Efficiency
* Matching current API design, conventions and patterns
* Consistent Reviewers
* Review is effective and making API designs simpler

```
They found the peerreviews to be more efficient than API usability tests, whilealso effectively highlighting usability issues in the API de-sign. Thus, providing a more scalable method for evaluatingAPIs. In their data, lab studies were 16 times more pro-ductive than peer reviews. However, the peer reviews weresubstantially faster and didn’t face the same resource prob-lems as lab studies
```

```
 This quick and contained back-and-forth di-rectly on the document allows feedback to be contained ina single source, with a trail of all conversation and decisionmaking logic. This approach isn’t without fault, as we reflecton in our analysis. Critically, the review remains iterative innature. Once both API owners and design reviewers agreeand sign-off on the API design, reviewers are then auto-matically assigned as reviewers on any future API changes(e.g. when an API moves from Beta to Generally Available,or if constraints elsewhere force a change to the originallyagreed upon design), this provides additional opportunity toreview the API, provide guidance on effective design, andensure that earlier feedback has been considered prior torelease, while also maintaining consistency. Critically, thishighlights that the review is not done after one linear passover the document, but rather continues to move and evolvethroughout the lifecycle of the API
```


```
Samples of end user source code is however essential, asit allows reviewers to see in practice how the API is used,the way in which calls are strung together, the level of ab-stractions chosen, etc. The Apiness review program usesheuristic evaluation, combined with knowledge of exist-ing Google API designs, to evaluate amongst other things,Casy Study: Design Methodology#chi4good, CHI 2016, San Jose, CA, USA852
naming conventions, level of abstraction, error messages,the resource model, the use of standard methods (GET,LIST, PUT, etc), and the use of common design patterns(e.g. pagination, long running operations, etc). Additionally,while also specifically evaluating the API in front of them,as previously mentioned, the Apiness reviewer is lookingfor consistency with existing Google APIs, and using preex-isting knowledge of potential usability issues to drive theirreviews. The Apiness team also goes beyond the surfaceof the API, looking also at the way in which an API will workwith Google’s programmatically generated client libraries
```
# Scratch


* [API Design Matters](https://queue.acm.org/detail.cfm?id=1255422)
* https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/32713.pdf

http://www.citeulike.org/


### Interviews

* Examples of API Design flaws that lead to undesired outcomes
* API Design process to reduce flaws


### Other
of case studies of API design flaws and

 that Software Quality and what we can learn from




Software Quality in this paper wil



 A well managed API life cycle process can help continually ensure that APIs meet desired quality goals.

While there are many APIs at all levels of the software stack this paper will focus on APIs that

This paper will focus on APIs that 

This paper will focus on three areas:

* API Quality
* API Design
* API life cycle

* What are the impacts of API design on developer productivity and software quality?
* What are the key pieces of an API?
* What are some solid API design principals?
* What is the API life cycle

## Pieces of an API

## Citations

### JavaScript == verses ===



[API Design and Why it matters](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/32713.pdf)




#### Notes

[Relational Algebra Model]: https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf "A Relation Model of Data form Large Shared Data Banks - E. F. Codd"


    Introduction of a Model

[Markdown]: https://commonmark.org/ "Markdown - CommonMark"

* Get Post Web Standard
* CPU Architecture



Exception Model:

throw
HRESULT
booleans
Error codes


#### Notes
Model did not solve the issue (not secure by default) Possible in C++ win encapsulated class.

strcpy API example
http://www.cplusplus.com/reference/cstring/strcpy/
strcpy_s



### Snapchat API

Snapchat API
https://apigee.com/about/blog/technology/api-mistakes-avoid
https://www.newyorker.com/tech/annals-of-technology/anatomy-of-a-snap-attack

Snapchat API Attack
https://gibsonsec.org/snapchat/
Release of users information

Combined wiht paper from reading

Poor behavior

[Robust De-anonymization of Large Datasets][Robust De-anonymization of Large Datasets]
Where releasing any user data is problamatic
