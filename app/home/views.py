from flask import render_template, abort
from flask_login import login_required
from jinja2 import TemplateNotFound

from . import home


# Homepage route
# ===============================================
@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    Guest are allowed to view the homepage BUT NOT submit reviews and rate books
    In the Homepage, users and guests can:
        - View lists of books
        - Search books, view info and reviews
    """
    try:
        return render_template('home/index.html', title="Welcome")
    except TemplateNotFound:
        abort(404)


# Profile page route
# ===============================================
@home.route('/profile')
@login_required
def profile():
    """
    Render the profile template on the /profile route
    Users must be logged in to view profile
    In the profile page, users can:
        - View list of books
        - Search books and view info and reviews
        - Rate and review books
    """
    try:
        return render_template('home/profile.html', title="My Books")
    except TemplateNotFound:
        abort(401)


# Book page route
# ===============================================
@home.route('/book/<string:isbn>')
def book():
    """
    Render the book template on the /book/isbn route
    """
    return render_template('home/book.html', title="Book")