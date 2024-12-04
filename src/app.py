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
    return


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
