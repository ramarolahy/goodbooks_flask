from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/book')
def book():
    return render_template("book.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/registration')
def registration():
    return render_template("registration.html")
