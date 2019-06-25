Upon faraday v3.8 we included an API Token for our api.
The token for the API will expire when the user changes the password.

The token can be retrieved when the user logs into the application using:

```
curl 'http://localhost:5985/_api/login'  -H 'Content-Type: application/json' --data-binary '{"email":"faraday","password":"changeme"}' --compressed
```

After successful login , the server will answer with a json that contains the api token.

```
{"code":200,"response":{"user":{"authentication_token":"WyIxIiwiJDUkcm91bmRzPTUzNTAwMCRHLkZQZUl0SjFEd0FsWjh2JEt5S01pS2h4elJJVzZUWmJVaTlzN2x1ZEx1eTVyZkxyM2E5V015QzB3QkMiXQ.XRJP_w.Pe9RBV0WAS6xOPrtHZUpx-j5MCY"}},"success":true}
```

Now that you got the auth token you can start using it on every request to the api:

```
curl 'http://localhost:5985/_api/v2/ws/wonderland' -H 'Authentication-Token:WyIxIiwiJDUkcm91bmRzPTUzNTAwMCRPeno4LkcvQmVwZm9nV0NuJHcxcE5pcXpCa1NtZTFFL05LTzBtTHpNdEZ2QVZVTkNEcUVaUG
43LjJoR0QiXQ.XRJQ1g.v21C5QNYZlMoM6M26_QLX7UAQc4'
```