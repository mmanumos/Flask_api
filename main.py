#!/usr/bin/python3
""" Flak app """
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    user_ip = request.remote_addr
    return "Hello world Platzi, this is your IP: {}".format(user_ip)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
