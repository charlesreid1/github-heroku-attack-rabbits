# Authenticate Users on Other Criteria

Suppose we wanted to do something silly like restrict
access to a page to users with Github handles that were 
between 5 and 7 letters.

Here is the relevant method that serves up `index.html` 
if the user's Github handle is 5-7 letters long:

```
@app.route('/')
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))

    resp = github.get("/user")

    if resp.ok:
        username = resp.json()['login']
        if len(username)>=5 and len(username)<=7:
            return send_from_directory(STATIC_PATH, 'index.html')

    return contents403
```



