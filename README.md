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

Final pages:

* The finished product (pages on Heroku protected by attack rabbits) 
    is at [github-heroku-attack-rabbits.herokuapp.com](https://github-heroku-attack-rabbits.herokuapp.com)

* The documentation is at [pages.charlesreid1.com/github-heroku-attack-rabbits](https://pages.charlesreid1.com/github-heroku-attack-rabbits)

Two branches in this repo compose the github-heroku-attack-rabbits documentation:

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
    contains the content that is actually pushed to Heroku - that is, 
    the final Flask app.


## Where do I start?

See the [documentation](https://pages.charlesreid1.com/github-heroku-attack-rabbits)
or [docs/index.md](docs/index.md).


## License

This is released under the [WTFPL](LICENSE).

