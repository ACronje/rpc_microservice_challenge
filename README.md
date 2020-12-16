# RPC Microservice Challenge

## Getting started

I recommend running the service with docker.

Start the service with docker-compose in one terminal:
```bash
docker-compose up
```

Run any of the RPC functions from another terminal:
```bash
docker exec -it rpc_microservice_challenge_rpc_microservice_1 ./entrypoint.sh nameko shell --config nameko_config.yml
```

## RPC functions

Square odd numbers:

```bash
➜  rpc_microservice_challenge git:(master) ✗ docker exec -it rpc_microservice_challenge_rpc_microservice_1 ./entrypoint.sh nameko shell --config nameko_config.yml
>>> n.rpc.service.square_odd_numbers(1,2,3)
[1, 9]
```

String compression:

```bash
➜  rpc_microservice_challenge git:(master) ✗ docker exec -it rpc_microservice_challenge_rpc_microservice_1 ./entrypoint.sh nameko shell --config nameko_config.yml
>>> n.rpc.service.compress_strings('Howdie', 'Hello', 'Hi')
{'Howdie': 'eJzzyC9PyUwFAAggAmE=', 'Hello': 'eJzzSM3JyQcABYwB9Q==', 'Hi': 'eJzzyAQAAPsAsg=='}
```

String decompression:

```bash
➜  rpc_microservice_challenge git:(master) ✗ docker exec -it rpc_microservice_challenge_rpc_microservice_1 ./entrypoint.sh nameko shell --config nameko_config.yml
>>> n.rpc.service.decompress_string('eJzzyC9PyUwFAAggAmE=')
'Howdie'
```

## What did I think of the task

Overall I found the task rather fun. It is always enjoyable for me to learn something new, so learning about RPC and string compression was definitely not a waste of my time.

I will just mention that the project outline was rather vague, specifically questions 2 and 3. It was not clear if these questions were related to one another, and also because no example inputs and outputs were given, I felt that these questions were open to interpretation (in case you are wondering, I _did_ send an email asking for clarification on these questions, but have not yet gotten a reply). Hopefully I understood and implemented them correctly!

For future assignments, it would be nice to have examples of inputs and expected outputs :)

## How I spent my time

Before even starting the assignment, I spent around an hour browsing over the Nameko documentation and going over some example projects to get an overview of the available features and how best to layout my small project.

I then spent around 30 mins setting up the project structure and got the sample service from the Nameko docs up and running in Docker, in order to avoid getting all the dependencies setup locally (I did not want to double my efforts).

With the sample project up and running in Docker, I was confident that I could now begin implementing the requested features. It took me around 30 mins to decide on the best compression library (I was not entirely sure what was expected of these functions as the assignment outline was a little vague), but then implementing the features was very straight-forward, and so I spent another hour on that.

In total the project took me around 3 hours.

## Thoughts on the tech used

Zlib:

Unfortunately for the examples I provided above, the strings were too short to really see the benefits of compression using zlib. In fact, after base64 encoding these compressed bytes so that they could be serialized by Nameko, some of them actually end up larger than they were without compression:
```python
>>> import base64
>>> import sys
>>> from rpc_microservice_challenge.lib.string_compression import compress_strings
>>> 
>>> string = "The quick brown fox jumped over arnoux's head..."
>>> sys.getsizeof(string)
97
>>> sys.getsizeof(compress_strings(string)[string])
89
>>> sys.getsizeof(base64.b64encode(compress_strings(string)[string]))
109
```

However, zlib's method of compression (called the DEFLATE lossless compression algorithm, which is a combination of the [LZ777 algorithm](https://en.wikipedia.org/wiki/LZ77_and_LZ78) and [Huffman encoding](https://en.wikipedia.org/wiki/Huffman_coding)) really shines on medium to large strings (> 100 bytes):
```python
>>> string = "The quick brown fox jumped over arnoux's head..." * 100
>>> sys.getsizeof(string)
4849
>>> sys.getsizeof(compress_strings(string)[string])
116
>>> sys.getsizeof(base64.b64encode(compress_strings(string)[string]))
145
```

If we were to only care about compressing small strings (< 100 bytes), then I would instead recommend that we use something like the [SMAZ small string compression algorithm](https://github.com/antirez/smaz) which is perfectly suited for this use case, and for my examples above, and for which there exists [at least one Python library](https://github.com/CordySmith/PySmaz). However the assignment overview was not clear on what size strings to expect, so I went with the compression lib that's already widely used and which is already available in the standard library.

RPC:

I watched an interesting [microservices talk](https://www.youtube.com/watch?v=IvsANO0qZEg) that talks about RPC vs other API implementation approaches (like REST and GraphQL) and the speaker mentioned some pros and cons that I agree with.

RPC is simple and easy to understand (we're just calling functions - no/few strict protocols to adhere to), payloads tend to be lightweight (functions are usually built for very specific purposes), and RPC "endpoints" have the potential to be highly performant (again because of the functions being built for very specific purposes, but also because we usually do not need to make multiple calls like with REST).

However RPC also has some disadvantages. There tends to be tighter coupling between the RPC "endpoints" and the underlying functions, there is no discoverability like there is with REST (discoverability being an awesome feature of REST that allows many frontend frameworks, like backbone, to give you out-of-the-box functions to consume your API), and often times, because there aren't many strict protocols on _how_ RPC "endpoints" should be structured, we can often end up in a place of "function explosion" where we create many similar functions that serve only slightly different purposes (and often these functions are poorly named!).

I think that as long as a team agrees on how they will layout their RPC services in a maintainable way, it can be a great way to quickly build microservices with efficient endpoints.

## Project design

This is a very small project so I didn't really think too deeply about design, but I did consider some things during implementation:
- I kept the code as functional as possible, since Nameko talks about being stateless and I ran with that.
- I did not put the base64 encoding/decoding in the compression/decompression functions because I believe those are view layer concerns (serialization). It would probably be a good idea to move this logic into functions in their own module if that code becomes used in more places.
- The project structure was inspired by [this article](https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6). It's been a while since I have had to work in Python so I googled until I found a structure that looked familiar.
- I used autopep8 and unify to auto-fix my code to be pep8 compliant.
