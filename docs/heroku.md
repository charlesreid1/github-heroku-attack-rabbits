# create heroku app


### Heroku toolbelt

Heroku offers a really nice command line interface tool called
Heroku Toolbelt. It is available through Homebrew and Aptitude:

```
$ brew install heroku   # from Mac

$ apt-get install heroku    # from Ubuntu
```

It is then available on the command line as `heroku`.

The first thing you should do is authenticate with
your Heroku account by running

```
$ heroku login
```

We will use this command line application for the following tasks:

* Create a git remote to point to the right Heroku git remote location
* Set environment variables (for e.g. secret keys) on the remote Heroku instance
* Get information (logs, status, etc.) about your Heroku app

We will cover these commands as they come up.


### Create heroku app

Start by creating a heroku app.

* Each heroku app must have a unique name
* Each heroku app creates a remote git repo
* Master branch is what Heroku deploys publicly on herokuapps.com
* You will also need heroku CLI to link your github repo to your heroku app


### Where heroku app lives

Suppose you are creating an app called `my-cool-app`
on heroku. Then your application will be hosted by 
Heroku and will be available at the URL:

```
https://my-cool-app.herokuapp.com
```

### How heroku apps works

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

