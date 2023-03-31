This is a script for a hackathon presentation about a soultion for visually-impaired people


OS suggestions in { } , comments in { } and italic.

## Hook

Tasks that take seconds for sighted people, can take several minutes for visually-impaired.

we are ajajajs and we are here to solve this problem.

## Problems

Solutions for the issues of visually-impaired people are very often
detached from reality. They are solutions that sound good but in practice
are useless.

what can I do with the information, that there is a tree

But the problems *we* are focusing on, are not that obvious but very needed.

Things like 
picking the right clothes from the closet
or 
differentiating between different packaged-goods.


It's things that sighted people don't even think about, that cause huge issues for visually-impaired.

[//]: # (While these things may be a routine for sighted people,)

[//]: # (they can pose a *significant* challenge for visually-impaired.)

Imagine differentiating between these T-shirts without your sight. Could you do it?

----

[//]: # (Univerzálnost řešení)

! So, why isn't this solved yet? 
 Well, one might think that this would be solved already by the generic image recognition applications. 

! But these solutions don't work well.

~ Due to their generality they *cannot* give information that is *precise enough* for these tasks.

> Víc emphasise že to fakt nejde

For example
~ if you want to distinguish between two T-shirts
the information that the T-shirts
are yellow is not enough ~ Or worse they can tell you it's a woman in a yellow dress.

----

We come with a solution. PAUSE

Instead of distinguishing between *all* the objects in the world we focus only on the things
that the user *owns*. With this we can achieve the precision that is needed.

Let's see how
this works.

A TADY BUDE DEMO

---- 

Using fine-tuned state-of-the-art image models. Such as OpenAI's CLIP.
We compute image embeddings and use those to find the most similar image in the user's
collection. With this we are able to achieve 97% accuracy on our test dataset.

Co je test dataset?


---
Závěr

There is no other app that does this {solves this problem?}. By recognizing only user-owned objects
we enable the visually impaired to recognize
everyday objects with the same ease as sighted people.

We demonstrated how this could work using our prototype, where the user first labels their items and
it enables them to recognize it afterward.

As we've discussed with Adam, Honza and Zuzka, the inability to distinguish among object of the same type is a serious problem for the visually impared.
And our application solves it.