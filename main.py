#!/usr/bin/python3
""" Flak app """
from flask import request, make_response, redirect
from flask import render_template, session, url_for, flash
import unittest

""" The app is creted from __init__ """
from app import create_app
""" The login form is imported """
from app.forms import LoginForm

app = create_app()


todos = ["Levantarse temprano", "Hacer ejercicio", "Terminar tutorial"]



@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

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
    session['user_ip'] = user_ip
    return response

@app.route("/hello", methods=['GET', 'POST'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = {
        "user_ip" : user_ip,
        "todos" : todos,
        "login_form" : login_form,
        "username" : username
    }

    """ POST """
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('Nombre de Usuario registrado')
        return redirect(url_for('index'))


    """ The context is sent in this way to use only the name of keys in the template """
    return render_template("hello.html", **context)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
