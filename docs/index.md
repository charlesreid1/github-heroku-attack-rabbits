# github-heroku-attack-rabbits

Protect secret pages hosted on Heroku by authenticating with Github using Flask-Dance. Also, attack rabbits.

![warning: attack rabbits ahead](img/warning.png)


## What's this business all about, then?

This repository helps you protect your secret pages by (deep breath):

hosting your secret page of static and/or dynamic content using a free Heroku app 
running a Python Flask server that uses Flask-Dance to authenticate visitors 
with Github which allows you fine-grained access control over your pages based on
user attributes like organization or team membership or even things like how many
repositories a user has or how many vowels are in their username. 

Also, did I mention the attack rabbits?


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

This is released under the [WTFPL](LICENSE).

