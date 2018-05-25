# Custom Domains

If you want to use a custom domain:

* Set up custom domain using Heroku command line interface
* This will set up a DNS subdomain specifically for your app
* Point your DNS records to the Heroku DNS subdomain

This also introduces complications with HTTP vs HTTPS:
OAuth must happen over HTTPS (required by protocol).
But you the user can control your domain and create 
SSL certificates for it, but Heroku is hosting the app.

You have two options: the free option, and the pay option.

**The pay option:** For $7/mo you can upgrade to hobby nodes,
which allows you to give Heroku permission to create an SSL 
certificate for your domain. This is the easiest solution
and requires zero setup, zero certificate management.

**The free option:** You can have your domain (HTTP only)
forward to Heroku (HTTPS can't be forwarded - that's ***key***). 
When you hit the Heroku domain, it will log the user in to Github. 
When the user logs in successfully, Github will redirect them to 
the callback URL. This callback URL ***MUST*** be HTTPS, so it cannot 
redirect back to your (HTTP-only) custom domain.

That means the userr will, after authenticating with Github,
always be redirected to `https://my-cool-app.herokuapp.com`
and never `http://my-cool-custom-domain-that-cannot-be-used-as-a-callback-because-it-is-https-only.com`.

The paid option is much, much simpler in the end 
and will save you $7/mo in setup time alone.
