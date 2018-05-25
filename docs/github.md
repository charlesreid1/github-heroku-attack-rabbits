## get started with github

We mentioned on the [heroku](heroku.md) page that heroku
creates a remote git repository to hold the files you 
want to host.

To use the contents of a Github repository on Heroku,
just treat it like another git remote, no special setup
is needed.

However, to set up your Github-Heroku attack rabbits to 
authenticate a user via Github, and mercilessly attack
all intruders, you must create a Github OAuth App.

### Creating Github OAuth App

Log into Github

Go to Settings

Click "Developer Settings" on the left side

Click  "New OAuth App" button in upper right

**What do these settings mean?**

* **Application name** is what will be shown to users when they visit
    a page protected by the attack rabbits and are prompted for
    their password by Github.

* **Homepage URL/Application description** are for users who want to know more 
    about your killer attack rabbit Github app

* **Authorization callback URL** is the URL that the users will be sent to
    once they authenticate with Github and they are granted an OAuth token.
    This is the magic ingredient that allows you to take actions on behalf
    of the account logging in.

In this guide we'll cover the case of checking membership in organizations or teams,
but what your attack rabbits end up doing to determine if a user is allowed to
access your secret pages is up to you.

### Shut up you twit and give me the values I need for the callback

So you're a little impatient to get started, huh?
No, hey, yeah, sure, y'know, that's totally understandable, 
I get it, you're eager to get some attack rabbits of your own.
That's fine, y'know, and I'll give you the callback you need to set
in just a minute, but before I do that, let me just give you some
advice about how you should best - 

(rough, shaky camera footage and screaming)

(black screen)

(fade in: camera zooms into a note held in the teeth of an attack rabbit)

```
callback:

http://localhost:5000/login/github/authorized

for testing locally only.

don't use HTTPS!
```

