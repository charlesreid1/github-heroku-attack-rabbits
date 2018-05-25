import os, json
from werkzeug.contrib.fixers import ProxyFix
from flask import Flask, redirect, url_for, send_from_directory
from flask_dance.contrib.github import make_github_blueprint, github
from os.path import join, isfile, isdir

# helpful:
# https://tinyurl.com/yddsw4pg

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
STATIC_PATH = 'content'

app = Flask(__name__)

# this worked locally, but not on heroku
app.wsgi_app = ProxyFix(app.wsgi_app)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "9502861d41e8729c5cae3225920b1b46")

app.config["RESULT_STATIC_PATH"] = STATIC_PATH #os.path.join(PROJECT_ROOT,STATIC_PATH)
app.config["GITHUB_OAUTH_CLIENT_ID"] = os.environ.get("GITHUB_OAUTH_CLIENT_ID")
app.config["GITHUB_OAUTH_CLIENT_SECRET"] = os.environ.get("GITHUB_OAUTH_CLIENT_SECRET")

github_bp = make_github_blueprint(
                        client_id = os.environ.get('GITHUB_OAUTH_CLIENT_ID'),
                        client_secret = os.environ.get('GITHUB_OAUTH_CLIENT_SECRET'),
                        scope='read:org')

app.register_blueprint(github_bp, url_prefix="/login")

contents200 = """
<html><body>
<div class="header header-20x">
<h1>Status: OK 200</h1>
</div>
<div class="body attack attack-rabbits">
<p>You found a public page, so you're safe for now. Run away while you still can.</p>
<p>Otherwise... the attack rabbits may find you yet.</p>
<img src="../img/warning.png" />
</div>
</body></html>
"""

contents403 = """
<html><body>
<div class="header header-40x">
<h1>Status: Error 403 Access Denied</h1>
</div>
<div class="body attack attack-rabbits">
<p>Access Denied!</p>
<p>Attack rabbits, attack! Prepare to meet your fate, 
sneaky unauthorized intruder, at the hands of one of
the nastiest, most horrible, gnashing teeth, and fangs, 
and little claws like daggers -</p>
<img src="../img/attack-rabbits.png" />
</div>
</body></html>
"""

contents404 = """
<html><body>
<div class="header header-40x">
<h1>Status: Error 404 Page Not Found</h1>
</div>
<div class="body attack attack-rabbits">
<p>The resource you requested could not be found.</p>
<p>The attack rabbits are circling, eyeing you suspiciously.</p>
<img src="../img/attack-rabbit.png" />
</div>
</body></html>
"""

@app.route('/')
def index():
    """
    the index, anybody can use
    """
    return send_from_directory(STATIC_PATH, 'index.html')


@app.route('/fishslap/')
def fishslap_even():
    if not github.authorized:
        return redirect(url_for("github.login"))

    resp = github.get("/user")
    if resp.ok:
        username = resp.json()['login']
        if even_vowels(username):
            #return "Hello {username}".format(username=username)
            fishslap = os.path.join(STATIC_PATH,'fishslap')
            return send_from_directory(fishslap, 'index.html')
    
    return contents403


@app.route('/sillywalk/')
def sillywalk_odd():
    if not github.authorized:
        return redirect(url_for("github.login"))

    resp = github.get("/user")
    if resp.ok:
        username = resp.json()['login']
        if not even_vowels(username):
            #return "Hello {username}".format(username=username)
            sillywalk = os.path.join(STATIC_PATH,'sillywalk')
            return send_from_directory(sillywalk, 'index.html')
    
    return contents403


@app.route('/<path:path>')
def all_github_users_welcome(path):
    """
    all other paths are public for anybody too
    """
    return send_from_directory(STATIC_PATH, path)
    

@app.errorhandler(404)
def oops(e):
    return contents404


def even_vowels(my_string):
    """
    Boolean: are there an even number of vowels in my_string?
    """
    i = 0
    for c in my_string:
        if c in list('aeiou'):
            i += 1
    if i%2==0:
        return True
    else:
        return False


if __name__ == "__main__":
    app.run()

