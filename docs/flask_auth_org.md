# Authenticate Users on Organization or Team Membership

Here is how we can make access to a given page or route
conditional on membership in an organization (in this 
example, membership in the `rainbow-mind-machine` organization
is required for access):

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
                return send_from_directory(STATIC_PATH, 'index.html')
```

