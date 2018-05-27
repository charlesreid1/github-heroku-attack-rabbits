# Testing Flask App Locally

We set up the Github App to use a callback of `https://localhost:5000/login/github/authorized`
so that we could test the app locally. Now it is time to test the app locally.

The application needs access to your Github app id and token. Those are provided 
via the `GITHUB_OAUTH_CLIENT_{ID,SECRET}` environment variables. Set these 
when you run the actual python command to run the server:

```
$ GITHUB_OAUTH_CLIENT_ID="xxxxxxx" \
  GITHUB_OAUTH_CLIENT_SECRET="xxxxxxx" \
  OAUTHLIB_INSECURE_TRANSPORT=true \
  python github.py
```

This runs the Flask server on port 5000, where it will wait for a visitor.
The way we have our application written in this example, the main `/` route
will redirect the user to a Github login screen immediately, but you could 
also present the user with a friendly welcome page when they go to `/`, 
and only redirect them to the Github login prompt when they visit a 
URL like `/login` or `/auth`.

Once you run the above command, open the following URL in your browser:

```
http://localhost:5000/
```

**NOTE: Make sure you are logged out of Github and that you clear your cookies 
if you are already logged in as one user and wish to authenticate as another.
The login is _very_ persistent so you may need to close and re-open your browser.**

Visiting the address above will result in your being redirected to a Github
login page. Once you login, Github will redirect the user back to the 
github-heroku-attack-rabbits application with a token that the application 
can use to perform actions on behalf of the user.

## Next Step?

If the app works, the next step is to deploy to Heroku.

