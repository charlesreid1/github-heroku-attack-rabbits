# Authenticate Users on Github Membership

For the sake of simplicity, will just demonstrate how this 
works for a single route, but you can combine different 
rules into multiple routes to provide access to different
people on different parts of a site.

Here is the relevant method that serves up `index.html` 
if the user is authenticated:

```
@app.route('/')
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))

    resp = github.get("/user")

    if resp.ok:
        return send_from_directory(STATIC_PATH, 'index.html')

    return contents403
```


