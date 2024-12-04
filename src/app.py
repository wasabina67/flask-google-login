import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, session

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html", user=session.get("user"))


@app.route("/login")
def login():
    request_uri = ""
    return redirect(request_uri)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
