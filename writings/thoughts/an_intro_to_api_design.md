# API Designs impact on Software Quality

## Thesis

Application Programming Interfaces (APIs) are the chief method for programmers to interact with software. APIs design can have a substantial impact on software quality.

This paper will examine API design flaws that lead to undesireable outcomes and analyze what could have been done to prevent these flaws.

This paper will examine:

* the general components of an API
* specific case studies where flaws in API design lead to undesireable outcomes
* an API design process to reduce API design flaws

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

__Mental models__ are the models that API users form in their head of how the API works. See [The Design of Everyday Things by Don Norman](http://www.nixdell.com/classes/HCI-and-Design-Spring-2017/The-Design-of-Everyday-Things-Revised-and-Expanded-Edition.pdf) for a full explanation of mental models. While Don Norman is generally describing interaction with physical objects the same concepts apply to API users.

Generally an API model is founded on both a technical model and a mental model.

### Structure

The structure of an API is the specific naming and parameters of function names, classes, interfaces, etc. that are used to interact with the API. The structure of an API is generally heavily influenced by its technical model as well as the mental model the API is attempting to represent.

### Behavior

The behavior and an API is what the API specifically does, or the effect that the API produces.


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



### Snapchat API


Snapchat API
https://apigee.com/about/blog/technology/api-mistakes-avoid
https://www.newyorker.com/tech/annals-of-technology/anatomy-of-a-snap-attack
Release of users information

### Windows GetVersion - compatibility

The Windows GetVersion API is an example where the API works as intended but the underlying versioning model is flawed.

Developers ended up using the API as a shortcut, Not as intended, additionally the APIs structure was flawed where developer could easily misuse the returned version. This caused many compatability issues where software that was capable of running on newer versions of the Operationg System were unable to run due to the check. In order to keep applications working the API had to be shimmed, and essentially ended up a a liability instead of an asset.

## API design process

The process of API design is a knowledge capture exercise. The goal is to capture as much information as possible into the APIs specification and clearly communicate that information to the implementers and users of the API.

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