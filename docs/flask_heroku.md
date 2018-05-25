# Deploying to Heroku

Once we have debugged the Flask app and we are happy with it,
we are ready to deploy it to Heroku. To deploy content to Heroku,
we just add our Heroku project as a git remote (see the [heroku](heroku.md)
page for how to do that) and then push to the master branch of the 
heroku remote git repo. Changes are pulled in by Heroku and the 
app is restarted each time you run git push.

## Heroku Login

From the `site/` directory containing the contents of the `heroku-pages` branch,
that is, containing the Python flask app, log in to Heroku:

```
heroku login
```


## Add Heroku Remote

Now have Heroku add the proper git remote address:

```
heroku git:remote -a <heroku-app-name>
```

Now you're ready to deploy to Heroku. 

## Deploy to Heroku

Double check your app is ready, then deploy:

```
git push heroku heroku-pages:master
```

This will push the local branch `heroku-pages` to
the remote branch `master` on the `heroku` remote.
This should begin a pre-commit hook where Heroku
compiles your Python app. You should get the green
light, if you tested your app locally and everything
was good to go.

## Check Your Heroku App

Your Heroku app will be available at 

```
https://<heroku-app-name>.herokuapp.com
```

You should see your Python flask app
show up shortly.

