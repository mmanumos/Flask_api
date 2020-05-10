#!/usr/bin/python3
""" Flak app """
from flask import Flask, request, make_response, redirect
from flask import render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
""" Config to generate a session with Flask """
app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ["Levantarse temprano", "Hacer ejercicio", "Terminar tutorial"]

class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')
    

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
        redirect(url_for('index'))


    """ The context is sent in this way to use only the name of keys in the template """
    return render_template("hello.html", **context)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
