from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from .forms import BookSearchForm, ReviewForm
from . import home
from ..models import *


def searchResults(category, value):
    """
    Function to search for books
    :return: render profile.html
    """
    form = BookSearchForm()
    results = []
    # books = Book.query.all()
    if category == 'isbn':
        results = Book.query.filter(Book.isbn.contains(value)).all()
    if category == 'author':
        results = Book.query.filter(Book.author.contains(value)).all()
    if category == 'title':
        results = Book.query.filter(Book.title.contains(value)).all()

    if not results:
        return redirect('/profile')
    else:
        return render_template('home/profile.html', form=form, results=results)


def createReview(book_isbn, user_id, rating, text):

    review = Review(book_isbn=book_isbn,
                    user_id=user_id,
                    rating=rating,
                    review_text=text
                )
    # Add the review to database
    db.session.add(review)
    db.session.commit()


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
        return searchResults(category, value)
    else:
        return render_template('home/profile.html', title="My Books", form=form)


# Book page route
# ===============================================
@home.route('/book/<string:isbn>', methods=['GET', 'POST'])
def book(isbn):
    """
    Render the book template on the /book/isbn route
    """
    # get book reviews
    reviews = Review.query.filter_by(isbn=isbn).all()

    # Check if current user  already submitted a review


    searchform = BookSearchForm()
    if searchform.validate_on_submit():
        category = searchform.select.data
        value = searchform.search.data
        return searchResults(category, value)

    reviewForm = ReviewForm()
    if reviewForm.validate_on_submit():
        book_isbn=isbn
        if current_user.is_authenticated:
            user_id = current_user.id
        rating = reviewForm.rating.data
        text = reviewForm.review.data
        createReview(book_isbn, user_id, rating, text)

    book = Book.query.filter_by(isbn=isbn).first()
    return render_template('home/book.html', title="Book", book=book, reviews=reviews, searchform=searchform, reviewForm=reviewForm)
