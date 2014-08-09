Rdnzl, my meta-cv
============================

Hi, my name is Florent Pastor. 
This is my meta-cv, which is a website coded with Django and Dart containing an interactive CV, 
but also a showcase of my skills with those two technologies.

It is running on [http://vps89599.ovh.net](http://vps89599.ovh.net).

This document will walk you through the project, specifying which of my skills were used for that project.

Git
---
I am used to the version control system Git. 

Clarifications to understand how my skills are shown by this repo : All you can see, for now, is simply one branch with two commits.
There is more : On my computer's repo, I have one other branch on which I developed the first version of the system. 
Around 20 commits were needed to complete the version, but since none of them except the last one represents interesting code,
I decided not to publish them in public, and to rebase and compress them on the branch master in one big commit.

Also, my computer's repo has two remotes : *origin*, this GitHub repo, and *private-origin*,
a repo stored on my [BitBucket](http://bitbucket.org/) account that contains all the branches on my computer's repo.
It allows me to save my work and to write code on other computers than mine.

In a future commit will also be expound my way of synchronising work between computers with that private git repo.

[Django](https://www.youtube.com/watch?v=IAooXLAPoBQ)
-----------------------------------------------------
This website uses Django in a basic way.
Two models, registered in the admin, linked together through another one and a few views responding, if they are called via Ajax, with JSON or with HTML.

If it is simple, I also believe it's a cleanly made, and easily extendable.
In a future commit, the server will be more complex : It will be internationalized to work in French and English,
will order its content in a more logical way and will generate a two minute tour of the CV based on a few \#skills the user gave him.

Dart
----
This is the first project I finish with Dart, the object oriented equivalent to Javascript. 
I made two objects that manage DOM elements that are provided to them on initialization :

* The first one handle the state of the page (Are we showing experiences or only the \#skills ?)
* The second one handle the Experience element : it update its content by requesting data to the server, change to the next or close it when there is no more experience

The usage of CSS
----------------
The script linked to the page are only changing the content and the classes of the page's elements.
The CSS is responsible of the designs and the animations. The concern are segregated.

Each state of the application has its URL. 
When you change the state of the application, by clicking a link, the content is loaded via Ajax and the URL is changed adequatly.
If you hit refresh, or send the URL to a friend, the page will load up in the same state.
