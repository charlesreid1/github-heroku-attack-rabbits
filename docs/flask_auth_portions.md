# Authenticate Different Users on Different Portions of Site

**NOTE: if you are authenticating using membership on a team, you will need the 
team id of the team you are interested in authenticating against.**

For this example, let's expand the routes we're looking at 
a bit more.

Suppose we have two folders, `team_only` and `org_only`.

The `team_only` folder should only be accessible to your team, `Team Gold`.

The `org_only` folder should only be accessible to your organization, `Colorful Colors`.

The main site (i.e., all other files) should be publicly accessible.

```python
@app.route('/')
def index():
    return send_from_directory(STATIC_PATH, 'index.html')


@app.route('/team_only/<path:path>')
def team_gold(path):

    if not github.authorized:
        return redirect(url_for("github.login"))

    rsp = app.config["RESULT_STATIC_PATH"]

    resp = github.get("/user")
    if resp.ok:
        username = resp.json()['login']

        team_id = 'XXXXX'

        resp = github.get("/teams/%s/members/%s"%( team_id, username ))
        if resp.code==204:
            team_gold_dir = os.path.join(STATIC_PATH, 'team_only')
            return send_from_directory(team_gold_dir, 'index.html')
    return contents403


@app.route('/org_only/<path:path>')
def team_gold(path):

    if not github.authorized:
        return redirect(url_for("github.login"))

    rsp = app.config["RESULT_STATIC_PATH"]

    resp = github.get("/user")
    if resp.ok:

        my_org = 'XXXXXXXX'

        all_orgs = resp.json()
        for org in all_orgs:
            if org['login']==my_org:
                color_org_dir = os.path.join(STATIC_PATH, 'org_only')
                return send_from_directory(color_org_dir, 'index.html')
    return contents403
```            

