# Initialize Git Repository

Let's talk through how a repository should be laid out 
if we're going to be hosting a Flask app on Heroku.

## Branches

We will need a minimum of two branches. Here we specify
the names that these branches will have in your Github repo,
**which is different from the names of the branches on Heroku**:

Branches on Github:

* `heroku-pages` - this branch contains the content that Heroku will host.
    Specifically, it contains the Flask application in a `.py` file, 
    and a few other files to help Heroku determine how to run the app
    and what to install.

* `master` - this branch contains the content used to generate the documentation
    and page content that is being hosted behind the Heroku attack sheep.
    The documentation you are reading right now is from the master branch,
    and was made with `mkdocs`.

On Heroku, we only have a single branch:

* `master` (Heroku) maps to `heroku-pages` (Github)

## Repo Layout

Let's talk about the layout of the repository.

If you wish to build the site in order to deploy it to Heroku,
you should clone the `master` branch (preparing to make the
content for your attack sheep-protected page):

```
$ git clone -b master https://git.charlesreid1.com/charlesreid1/github-heroku-attack-rabbits.git
$ cd github-heroku-attack-rabbits
```

Once you are *inside* the master branch, clone the repo again,
but this time clone the `heroku-pages` branch, and clone it 
to the `site/` folder:

```
$ git clone -b heroku-pages https://git.charlesreid1.com/charlesreid1/github-heroku-attack-rabbits.git site
$ cd site
```

Now you will want to set up the Heroku remote:

```
$ heroku git:remote -a my-cool-project
```

The layout should now be:

```
my-cool-project-repo/   <-- my-cool-project repo pointing to master branch

        docs/            \
            index.md      |
            heroku.md     | <-- mkdocs files 
            ...           |     (can use any static content generator:
                          |      pelican, sphinx, etc.)
        mkdocs.yml       /
        
        site/           <-- my-cool-project repo pointing to heroku-pages branch
            
            Procfile           \ 
            github.py           | <-- heroku python app files
            requirements.txt    |     (can also use ruby, php, js, etc.)
            runtime.txt         |     (can also use ruby, php, js, etc.)
            ...                / 

            content/           \   
                index.html      | <-- static content hosted by Flask
                sitemap.xml     | 
                ...            /  
```


## Workflow

Once you have things set up according to the instructions and diagram above,
you're ready to run the push-to-deploy workflow and start running your secret
site on Heroku.























