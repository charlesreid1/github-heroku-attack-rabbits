# Create a Heroku app

## Before you begin: install Heroku toolbelt

Heroku offers a really nice command line interface tool called
Heroku Toolbelt. It is available through Homebrew and Aptitude:

```plain
$ brew install Heroku   # from Mac

$ apt-get install Heroku    # from Ubuntu
```

It will then be available on the command line as `Heroku`.

The first thing you should do is authenticate with
your Heroku account by running

```plain
$ heroku login
```

We will use this command line application for the following tasks:

* Create a git remote to point to the right Heroku git remote location
* Set environment variables (for e.g. secret keys) on the remote Heroku instance
* Get information (logs, status, etc.) about your Heroku app

We will cover these commands as they come up.


## Creating a Heroku app

Start by creating a Heroku app.

* Each Heroku app must have a unique name
* Each Heroku app creates a remote git repo
* Master branch is what Heroku deploys publicly on Herokuapps.com
* You will also need Heroku CLI to link your github repo to your Heroku app


## Where Heroku apps live

Suppose you are creating an app called `my-cool-app`
on Heroku. Then your application will be hosted by 
Heroku and will be available at the URL:

```plain
https://my-cool-app.herokuapp.com
```

### How Heroku apps work

If you have used Github Pages before, Heroku uses a similar
model (live hosting one particular branch of a git repository).
However, Heroku is different because you can run dynamic scripts
using Python, Ruby, PHP, etc.

To change the content of your Heroku app, just change the contents
of the repository, and push to master (push to the master branch of
the remote Heroku repository).

You will need to structure your repository carefully.
That's what this page is here to help you do.
Heroku can figure out the rest from there.

