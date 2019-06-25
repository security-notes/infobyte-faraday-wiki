Upon faraday v3.8 we included an API Token for our api.
The token for the API will expire when the user changes the password.

The token can be retrieved when the user logs into the application using:

```
curl 'http://localhost:5985/_api/login'  -H 'Content-Type: application/json' --data-binary '{"email":"faraday","password":"changeme"}' --compressed
```

After successful login , the server will answer with a json that contains the api token.

```
{"code":200,"response":{"user":{"authentication_token":"AUTH_TOKEN"}},"success":true}
```

Now that you got the auth token you can start using it on every request to the api:

```
curl 'http://localhost:5985/_api/v2/ws/wonderland' -H 'Authentication-Token:AUTH_TOKEN'
```