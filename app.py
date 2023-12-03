import os
import datetime
from flask import Flask


app = Flask(__name__)
@app.route("/")
def hello_world():
    hostname=os.getenv("HOSTNAME")
    dtstr = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    # return f"<p>Hello World~! from {hostname}</p>"
    return f"<p>Hello World~! (V1) From: {hostname} {dtstr}</p>"