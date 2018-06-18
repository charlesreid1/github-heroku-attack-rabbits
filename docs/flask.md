# Create a Flask App using Flask-Dance

This is the heart of the method.

The best thing to do here is just to walk you through the script.

Import statements:

```python
import os, json
from os.path import join, isfile, isdir
from werkzeug.contrib.fixers import ProxyFix
from flask import Flask, redirect, url_for, send_from_directory
from flask_dance.contrib.github import make_github_blueprint, github
```

Note that flask-dance adds an OAuth login/callback route 
to your Flask app by creating a `/login` blueprint,
meaning all the OAuth stuff is just magically available 
via `/login`.

Set paths for static content:

```python
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
STATIC_PATH = 'content'
```

Create and configure app. This requires confidential information
for the Github application you created, specifically the client
ID and client secret. These are at the very top of the page when
you visit your app's settings page.

To find this, after you log in, click your profile photo in the
upper right > Settings > Developer Settings > OAuth Apps > click the 
name for your OAuth app.

```python
app = Flask(__name__)

# this worked locally, but not on heroku
app.wsgi_app = ProxyFix(app.wsgi_app)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "9502861d41e8729c5cae3225920b1b46")

app.config["RESULT_STATIC_PATH"] = STATIC_PATH #os.path.join(PROJECT_ROOT,STATIC_PATH)
app.config["GITHUB_OAUTH_CLIENT_ID"] = os.environ.get("GITHUB_OAUTH_CLIENT_ID")
app.config["GITHUB_OAUTH_CLIENT_SECRET"] = os.environ.get("GITHUB_OAUTH_CLIENT_SECRET")
```

Now the magic happens: we use flask-dance to create a blueprint
that has methods and settings all ready to go for us to do the 
OAuth dance.

`make_github_blueprint()` is part of the contrib module of flask-dance.
There are several similar methods to generate blueprints for 
authenticating with other APIs.

```python
github_bp = make_github_blueprint(
                        client_id = os.environ.get('GITHUB_OAUTH_CLIENT_ID'),
                        client_secret = os.environ.get('GITHUB_OAUTH_CLIENT_SECRET'),
                        scope='read:org')

app.register_blueprint(github_bp, url_prefix="/login")

contents404 = "<html><body><h1>Status: Error 404 Page Not Found</h1></body></html>"
contents403 = "<html><body><h1>Status: Error 403 Access Denied</h1></body></html>"
contents200 = "<html><body><h1>Status: OK 200</h1></body></html>"
```

Deal with the `/` route first:

* Check if authorized, if not, redirect them to the login URL
    (magical URLs taken care of magically by our `make_github_blueprint`
    function above)
* If user is authorized (i.e., if they have gone through the OAuth 
    process and given their passsword to Github and been redirected 
    to your app with an OAuth token), then the next step is to 
    find out some information about them.
* Use the `github` object to call the Github API directly.
* Decide what to do from there.

```python
@app.route('/')
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))

    resp = github.get("/user/orgs")
    if resp.ok:

        all_orgs = resp.json()
        for org in all_orgs:
            if org['login']=='rainbow-mind-machine':
```

The next line is important to how the server works:
if all of the criteria above have been met, we return 
a static file:

```python
                return send_from_directory(STATIC_PATH, 'index.html')
```

This is normally "bad practice," and numerous type A people 
on the internet will tell you Flask should not be used for 
serving static files, and that you should use nginx etc., 
but these fail to igonore the following:

* Heroku does not let you run or configure nginx
* For crying out loud this example is about attack rabbits 
    stop taking everything so seriously

Now that we've got that out of the way...

Here's how we serve up static files. This is a total hack,
but it works. It takes any arbitrary path supplied by the 
user, and attempts to find a corresponding file to serve up
on disk. 

If the user passes a file, then that file is served up.

If the user passes a directory, then `index.html` is served up.

If the user asks for a non-existent file, a 404 error is shown.

If the user is not allowed to view the content, they will face 
the bowel-emptying terrors of the 403 error.

```python
@app.route('/<path:path>')
def catch_all(path):
    
    if not github.authorized:
        return redirect(url_for("github.login"))

    username = github.get("/user").json()['login']

    rsp = app.config["RESULT_STATIC_PATH"]
    resp = github.get("/user/orgs")
    if resp.ok:

        all_orgs = resp.json()
        for org in all_orgs:
            if org['login']=='dcppc':

                if(path==''):
                    return send_from_directory(rsp, 'index.html')

                elif(isdir(join(rsp,path))):
                    return send_from_directory(join(rsp,path),'index.html')

                elif(isfile(join(rsp,path))):
                    return send_from_directory(rsp, path)

                else:
                    return contents404

    return contents403
```

Last, set a default 404 handler, and run the app:

```python
@app.errorhandler(404)
def oops(e):
    return contents404


if __name__ == "__main__":
    app.run()
```

