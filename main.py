#!/usr/bin/python3
""" Flak app """
from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

todos = ["Levantarse temprano", "Hacer ejercicio", "Terminar tutorial"]

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)

@app.errorhandler(500)
def not_found(error):
    return render_template("500.html", error=error)


@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    response.set_cookie("user_ip", user_ip)
    return response

@app.route("/hello")
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        "user_ip" : user_ip,
        "todos" : todos
    }
    """ The context is sent in this way to use only the name of keys in the template """
    return render_template("hello.html", **context)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
