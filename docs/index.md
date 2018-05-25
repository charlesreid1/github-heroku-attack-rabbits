# github-heroku-attack-rabbits

## What's this business all about, then?

This repository helps you protect your secret pages by (deep breath):

hosting your secret page of static and/or dynamic content using a free Heroku app 
running a Python Flask server that uses Flask-Dance to authenticate visitors 
with Github which allows you fine-grained access control over your pages based on
user attributes like organization or team membership or even things like how many
repositories a user has or how many vowels are in their username. 

Also, did I mention the attack rabbits?

![warning: attack rabbits ahead](img/warning.png)


## Where is everything?

Two branches document how github-heroku-attack-rabbits work:

* (**YOU ARE HERE**) The [docs](https://git.charlesreid1.com/charlesreid1/github-heroku-attack-rabbits/src/branch/docs) branch 
    contains the files needed to generate the 
    [github-heroku-attack-rabbits documentation site](https://pages.charlesreid1.com/github-heroku-attack-rabbits).

* The [gh-pages](https://git.charlesreid1.com/charlesreid1/github-heroku-attack-rabbits/src/branch/gh-pages) branch
    contains the static files generated from the documentation.
    The contents of this branch compose the 
    [github-heroku-attack-rabbits documentation site](https://pages.charlesreid1.com/github-heroku-attack-rabbits).

Two branches illustrate github-heroku-attack-rabbits in practice:

* The [secret](https://git.charlesreid1.com/charlesreid1/github-heroku-attack-rabbits/src/branch/secret) branch contains the files needed to create the secret page. 
    This repository is public, so obviously these aren't *actually* secret,
    but in practice this would be in a protected repository.

* The [heroku-pages](https://git.charlesreid1.com/charlesreid1/github-heroku-attack-rabbits/src/branch/heroku-pages) branch


## Contents

An overview of the steps:

[Get Started with Heroku](heroku.md)

[Get Started with Github](github.md)

[Initialize Repository: Branches](repo.md)

[Create a Flask App using Flask-Dance](flask.md)

* [Authenticate users based on Github membership only](flask_auth_github.md)
* [Authenticate users based on organization or team membership](flask_auth_org.md)
* [Authenticate users based on some other criteria](flask_auth_other.md)
* [Protection portions of the site](flask_auth_portions.md)

[Test Flask App Locally](flask_local.md)

[Deploying Flask App to Heroku](flask_heroku.md)

[Custom Domains](custom_domains.md)


## Links

Python software used:

* [Flask](http://flask.pocoo.org/)
* [Flask-dance](https://github.com/singingwolfboy/flask-dance)
* [Flask-dance-github](https://github.com/singingwolfboy/flask-dance-github)
* [mkdocs-material (documentation theme)](https://github.com/squidfunk/mkdocs-material)
* [mkdocs (documentation)](http://www.mkdocs.org/)

Commercial services:

* [Heroku](https://heroku.com)
* [Github](https://github.com)


## License

This is released under the [WTFPL](https://git.charlesreid1.com/charlesreid1/github-heroku-attack-rabbits/src/branch/docs/LICENSE).
