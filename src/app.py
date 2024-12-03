import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def index():
    return "index"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
