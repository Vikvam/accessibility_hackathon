This is a script for a hackathon presentation about a soultion for visually-impaired people

## Hook

Tasks that take seconds for sighted people, can take several minutes for visually-impaired.

## Problems

The issues visually-impaired have, that sighted people first think of such as

- crossing the road
- a tenhle
- a tenhle

are mostly dealt with. But the problems we are focusing on, are not that obvious.
Things like picking the right clothing or differentiating between different packaged-goods.

přidat sem, že nás to ani nenapadne

[//]: # (While these things may be a routine for sighted people,)

[//]: # (they can pose a *significant* challenge for visually-impaired.)

Imagine differentiating between these T-shirts without your sight. Could you do it?

----

So, why isn't this solved yet? Well, one might think that this would be solved
by the generic image recognition applications. But these solutions don't work well.

Due to their generality they *can't* give information that is precise enough. For example
if you want to distinguish between two yellow T-shirts the information that the T-shirts
we are holding is not enough. Or worse it can tell you it's a women in a yellow dress.

----

We come with a solution. PAUSE

Instead of distinguishing between all the objects in the world we focus only on the things
that the user owns. With this we can achieve the precision that is needed. Let's see how
this works.

A TADY BUDE DEMO

---- 

Using fine-tuned state-of-the-art image models. Such as OpenAI's CLIP.
We compute image embeddings and use those to find the most similar image in the user's
collection. With this we are able to achieve 97% accuracy on our test dataset.


---
Závěr

There is no other app that does this. By recognizing only user-owned obejcts
we enable the visually impaired to recognize
everyday objects with the same ease as sighted people.

We created a working prototype, ... nevím

As we discussed with "names" this is something that visually impaired people are missing. 

