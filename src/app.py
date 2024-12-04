import os

import requests  # type: ignore
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, session
from oauthlib.oauth2 import WebApplicationClient  # type: ignore

from utils import get_openid_configuration

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

client_id = os.getenv("GOOGLE_CLIENT_ID")
client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
openid_configuration = get_openid_configuration(
    os.getenv("GOOGLE_OPENID_CONFIGURATION")
)
authorization_endpoint = openid_configuration["authorization_endpoint"]
token_endpoint = openid_configuration["token_endpoint"]
userinfo_endpoint = openid_configuration["userinfo_endpoint"]
redirect_uri = "https://localhost:3443/callback"
scope = ["openid", "email", "profile"]

client = WebApplicationClient(client_id)


@app.route("/")
def index():
    return render_template("index.html", user=session.get("user"))


@app.route("/login")
def login():
    request_uri = client.prepare_request_uri(
        uri=authorization_endpoint,
        redirect_uri=redirect_uri,
        scope=scope,
    )
    return redirect(request_uri)


@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "Error: No code provided", 400

    request_url = request.url
    authorization_response = request_url.replace(
        "http://localhost/callback", redirect_uri
    )
    token_url, headers, body = client.prepare_token_request(
        token_url=token_endpoint,
        authorization_response=authorization_response,
        redirect_url=redirect_uri,
        code=code,
    )

    token_response = requests.post(
        url=token_url,
        data=body,
        headers=headers,
        auth=(client_id, client_secret),
    )
    client.parse_request_body_response(token_response.text)

    url, headers, body = client.add_token(userinfo_endpoint)
    user_info = requests.get(url=url, data=body, headers=headers).json()

    print(user_info)

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
