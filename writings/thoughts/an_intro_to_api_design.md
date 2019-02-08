# API Designs impact on Software Quality

## Thesis

Application Programming Interfaces (APIs) are the chief method for programmers to interact with software. APIs design can have a substantial impact on software quality.

This paper will examine API design flaws that lead to undesireable outcomes and analyze what could have been done to prevent these flaws.

This paper will examine:

* the general components of an API
* specific case studies where flaws in API design lead to undesireable outcomes
* examine an API design process to reduce API design flaws

## API Components

Before examining specific cases where API design flaws lead to undesireable outcomes it is worth examining the components of an API to better understand the causes of the design flaw. 

* Model
* Structure
* Behavior

### Model

#### Definition

The model of an API is it's underlying paradigm. The model consists of both a underlying technical model as well as mental model of the APIs meaning.

#### Explanation

Technical API models are usually well documented models such as:

* the [Relational Model][Relational Algebra Model] that backs most modern databases
* CPU Architecture x86, AMD64, ARM which describe how to interact with a CPU
* Get Post Web Models
* 
* Languages: JavaScript, C, C++

#### Notes

[Relational Algebra Model]: https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf "A Relation Model of Data form Large Shared Data Banks - E. F. Codd"
    Introduction of a Model

[Markdown]: https://commonmark.org/ "Markdown - CommonMark"

* Get Post Web Standard
* CPU Architecture


### Structure


### Behavior

How to specify behavior?


## Case Studies

Now that we have examined the components 

### C / C++ strcpy

#### Undesireable Outcome

#### Notes
Model did not solve the issue (not secure by default) Possible in C++ win encapsulated class.

strcpy API example
http://www.cplusplus.com/reference/cstring/strcpy/
strcpy_s


[Control Flow Guard]: https://docs.microsoft.com/en-us/windows/desktop/secbp/control-flow-guard

### NASA’s Mars Climate Orbiter - Spacecraft Metric to Imperial units

https://en.wikipedia.org/wiki/Mars_Climate_Orbiter
"produced output in non-SI units of pound-force seconds (lbf·s) instead of the SI units of newton-seconds (N·s) specified in the contract between NASA and Lockheed."

"The primary cause of this discrepancy was that one piece of ground software supplied by Lockheed Martin produced results in a United States customary unit, contrary to its Software Interface Specification (SIS), while a second system, supplied by NASA, expected those results to be in SI units, in accordance with the SIS. Specifically, software that calculated the total impulse produced by thruster firings produced results in pound-force seconds. The trajectory calculation software then used these results – expected to be in newton seconds – to update the predicted position of the spacecraft.[16] Still, NASA does not place the responsibility on Lockheed for the mission loss; instead; various officials at NASA have stated that NASA itself was at fault for failing to make the appropriate checks and tests that would have caught the discrepancy"

### Snapchat API


Snapchat API
https://apigee.com/about/blog/technology/api-mistakes-avoid
https://www.newyorker.com/tech/annals-of-technology/anatomy-of-a-snap-attack
Release of users information

### Windows GetVersion - compatibility

The Windows GetVersion API is an example where the API works as intended but the underlying versioning model is flawed.

Developers ended up using the API as a shortcut, Not as intended, additionally the APIs structure was flawed where developer could easily misuse the returned version. This caused many compatability issues where software that was capable of running on newer versions of the Operationg System were unable to run due to the check. In order to keep applications working the API had to be shimmed, and essentially ended up a a liability instead of an asset.

## API design process



* [API Design Matters](https://queue.acm.org/detail.cfm?id=1255422)
* https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/32713.pdf

## Conclusion

Analysis of where to prevent issues common causes









## Scratch

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


