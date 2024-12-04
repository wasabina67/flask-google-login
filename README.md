# flask-google-login
Flask Google login

## Setup

- [OAuthLib](https://oauthlib.readthedocs.io/en/latest/)
- [oauthlib/oauthlib](https://github.com/oauthlib/oauthlib)

### Redirect URI

```
https://localhost:3443/callback
```

### Create .env

```bash
cp -p .env.example .env
```

- SECRET_KEY
  - Flask secret key
- CLIENT_ID
- CLIENT_SECRET
- GOOGLE_OPENID_CONFIGURATION

## Run

```bash
python src/app.py
```

Open https://localhost:3443/
