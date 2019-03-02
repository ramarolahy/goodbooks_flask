from flask import render_template, abort, request, flash, redirect
from flask_login import login_required
from jinja2 import TemplateNotFound


from .forms import BookSearchForm
from . import home
from ..models import *


def search_results(category, value):
    """
    Function to search for books
    :return: render results.html
    """
    form = BookSearchForm()
    results = []
    # books = Book.query.all()
    if category == 'ISBN':
        results = Book.query.filter(Book.isbn.contains(value)).all()
    if category == 'Author':
        results = Book.query.filter(Book.author.contains(value)).all()
    if category == 'Title':
        results = Book.query.filter(Book.title.contains(value)).all()

    if not results:
        flash('No results found!', 'warning')
        return redirect('/profile')
    else:
        return render_template('home/profile.html', form=form, results=results)

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
    return render_template('home/index.html', title="Welcome")

# Profile page route
# ===============================================
@home.route('/profile', methods=['GET', 'POST'])
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
    form = BookSearchForm()

    if form.validate_on_submit():
        category = form.select.data
        value = form.search.data
        return search_results(category, value)

    return render_template('home/profile.html', title="My Books", form=form)

# Book page route
# ===============================================
@home.route('/book/<string:isbn>', methods=['GET', 'POST'])
def book(isbn):
    """
    Render the book template on the /book/isbn route
    """
    form = BookSearchForm()
    if form.validate_on_submit():
        category = form.select.data
        value = form.search.data
        return search_results(category, value)

    book = Book.query.filter_by(isbn=isbn).first()
    return render_template('home/book.html', title="Book", book=book, form=form)