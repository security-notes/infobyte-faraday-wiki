Upon faraday v3.9 we included an API Token for our api.
The token for the API will expire when the user changes the password.

You can configure token expiration in the `[server]` section of the configuration with the option `api_token_expiration` expressed in seconds.

Token expires by timeout or when the user changes the password.
Each token is associated to the user who requests the token.

The token can be retrieved when the user logs into the application using:

```
curl 'http://localhost:5985/_api/login'  -H 'Content-Type: application/json' --data-binary '{"email":"faraday","password":"changeme"}' --compressed -c cookie.txt
```

After successful login , you can get the token using the token api:

```
curl 'http://localhost:5985/_api/v2/token/' -b cookie.txt
```

The token endpoint will return a token:

```
eyJhbGciOiJIUzUxMiIsImV4cCI6MTU2Mjc4MzQwOCwiaWF0IjoxNTYyNzc5ODA4fQ.eyJ1c2VyX2lkIjoxfQ.7Ha87yAFi5OFsTJUocgQOpsy3NfHlBRRI2449HvgU_GcywdZTzrW1kdWkX4vo4A84Ki7Hb-VnsLaHwD_Ei7R6Q
```

Now that you got the auth token you can start using it on every request to the api:

```
curl 'http://localhost:5985/_api/v2/ws/' -H 'Authorization:Token AUTH_TOKEN' -H 'Content-Type: application/json' 
```