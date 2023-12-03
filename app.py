import os
from flask import Flask


app = Flask(__name__)
@app.route("/")
def hello_world():
    hostname=os.getenv("HOSTNAME")
    return f"<p>Hello World~! from {hostname}</p>"