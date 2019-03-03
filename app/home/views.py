from flask import render_template, request, redirect, url_for, flash
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

    if category == 'isbn':
        results = Book.query.filter(Book.isbn.contains(value)).all()
    if category == 'author':
        results = Book.query.filter(Book.author.contains(value)).all()
    if category == 'title':
        results = Book.query.filter(Book.title.contains(value)).all()

    if not results:
        #flash('No books where found!', 'warning')
        return redirect(url_for('home.profile', reader=current_user.first_name))

    else:
        return render_template('home/results.html', form=form, results=results)



def createReview(review_date, book_isbn, reader_id, rating, title, text):
    book = Book()
    reader = Reader()
    review = Review(review_date=review_date,
                    book_isbn=book_isbn,
                    reader_id=reader_id,
                    rating=rating,
                    review_title=title,
                    review_text=text
                    )
    # Add the review to database
    db.session.add(review)
    reader.books_reviewed.append(book)
    db.session.add(reader)
    db.session.commit()
    redirect('/book/<string:isbn>')



# Homepage route
# ===============================================
@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    Guest are allowed to view the homepage BUT NOT submit reviews and rate books
    In the Homepage, readers and guests can:
        - View lists of books
        - Search books, view info and reviews
    """
    return render_template('home/index.html', title="Welcome")


# Profile page route
# ===============================================
@home.route('/profile/<string:reader>', methods=['GET', 'POST'])
@login_required
def profile(reader):
    """
    Render the profile template on the /profile route
    Users must be logged in to view profile
    In the profile page, readers can:
        - View list of books
        - Search books and view info and reviews
        - Rate and review books
    """
    # On first load, display default results
    reviews = Review.query.filter_by(reader_id=current_user.id).all()
    #booksReviewed = Book.query.join(Book.user_reviews, Book.users).filter_by(user.id=current_user.id).all()

    form = BookSearchForm()
    if form.validate_on_submit():
        category = form.select.data
        filter = form.search.data
        results = searchResults(category, filter)
        return results
    else:
        return render_template('home/profile.html', title="My Books", form=form, reviews=reviews)


# Profile page route
# ===============================================
@home.route('/results/<string:category><string:filter>', methods=['GET', 'POST'])
@login_required
def results(category, filter):
    """
    Render the profile template on the /profile route
    Users must be logged in to view profile
    In the profile page, users can:
        - View list of books
        - Search books and view info and reviews
        - Rate and review books
    """
    results = []
    form = BookSearchForm()
    if form.validate_on_submit():
        category = form.select.data
        filter = form.search.data
        results = searchResults(category, filter)
        return results
    else:
        return render_template('home/results.html', title="My Books", form=form, results=results)

# Book page route
# ===============================================
@home.route('/book/<string:isbn>', methods=['GET', 'POST'])
@login_required
def book(isbn):
    """
    Render the book template on the /book/isbn route
    """

    # get book reviews
    reviews = Review.query.filter_by(book_isbn=isbn).all()
    # Still trying to figure out relationships and foreignkeys so this is just a workaround
    readers = Reader.query.all()

    # Find out if current reader already reviewed the current book.
    # Returns None if current_user was not found
    didReview = Review.query.filter_by(book_isbn=isbn, reader_id=current_user.id).one_or_none()
    book = Book.query.filter_by(isbn=isbn).first()

    searchform = BookSearchForm()
    if searchform.validate_on_submit():
        category = searchform.select.data
        value = searchform.search.data
        return searchResults(category, value)

    reviewForm = ReviewForm()
    if reviewForm.validate_on_submit():
        review_date = datetime.now()
        book_isbn = isbn
        reader_id = current_user.id
        rating = reviewForm.rating.data
        title = reviewForm.title.data
        text = reviewForm.review.data
        createReview(review_date, book_isbn, reader_id, rating, title, text)

    return render_template('home/book.html', title="Book", book=book, reviews=reviews,
                           searchform=searchform, reviewForm=reviewForm, readers=readers, didReview=didReview
                           )
