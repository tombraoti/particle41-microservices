# save this as app.py
from flask import Flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    ip_address = flask.request.remote_addr
    return "Requester IP: " + ip_address

app.run(host="0.0.0.0", port=8080)
