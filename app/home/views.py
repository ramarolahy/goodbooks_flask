import requests
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user


from .forms import BookSearchForm, ReviewForm
from . import home
from ..models import *



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
    booksReviewed = current_user.books_reviewed

    return render_template('home/profile.html', title="My Books", reviews=reviews, booksReviewed=booksReviewed, active='home')



    #redirect(url_for('home.results', category=category, filter=filter, results=results))


# Profile page route
# ===============================================
@home.route('/results/', methods=['GET', 'POST'])
@login_required
def results():
    """
    Render the profile template on the /profile route
    Users must be logged in to view profile
    In the profile page, users can:
        - View list of books
        - Search books and view info and reviews
        - Rate and review books
    """
    results = Book.query.all()

    def searchResults(category, filter):
        if category == 'isbn':
            results = Book.query.filter(Book.isbn.contains(filter)).all()
        if category == 'author':
            results = Book.query.filter(Book.author.contains(filter)).all()
        if category == 'title':
            results = Book.query.filter(Book.title.contains(filter)).all()
        return results

    form = BookSearchForm()
    if form.validate_on_submit():
        results =searchResults(form.select.data, form.search.data)

    return render_template('home/results.html', title="My Books", form=form, results=results, active='search')


def createReview(review_date, book_isbn, reader_id, rating, title, text):
    review = Review(review_date=review_date,
                    book_isbn=book_isbn,
                    reader_id=reader_id,
                    rating=rating,
                    review_title=title,
                    review_text=text
                    )
    # get the book being reviewed
    reviewed_book = Book.query.filter_by(isbn=book_isbn).first()
    # Add the review to database
    db.session.add(review)
    # add the book to the current_user's books_reviewed (association_table)
    current_user.books_reviewed.append(reviewed_book)
    db.session.commit()



# Book page route
# ===============================================
@home.route('/book/<string:isbn>', methods=['GET', 'POST'])
@login_required
def book(isbn):
    """
    Render the book template on the /book/isbn route
    """
    GOODREADS_API_KEY = "JzDtAyR5qcTeAuhFKOHSw"

    res = requests.get("https://www.goodreads.com/book/review_counts.json",
                       params={"key": GOODREADS_API_KEY, "isbns": isbn})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    ratings = data['books'][0]['work_ratings_count']
    average_rating = data['books'][0]['average_rating']

    # get book reviews
    reviews = Review.query.filter_by(book_isbn=isbn).all()
    # Still trying to figure out relationships and foreignkeys so this is just a workaround
    readers = Reader.query.all()

    # Find out if current reader already reviewed the current book.
    # Returns None if current_user was not found
    didReview = Review.query.filter_by(book_isbn=isbn, reader_id=current_user.id).one_or_none()
    book = Book.query.filter_by(isbn=isbn).first()



    reviewForm = ReviewForm()
    if reviewForm.validate_on_submit():
        review_date = datetime.now()
        book_isbn = isbn
        reader_id = current_user.id
        rating = reviewForm.rating.data
        title = reviewForm.title.data
        text = reviewForm.review.data
        createReview(review_date, book_isbn, reader_id, rating, title, text)
        return redirect(url_for('home.profile', reader=current_user.first_name))

    return render_template('home/book.html', title="Book", book=book, reviews=reviews,
                            reviewForm=reviewForm, readers=readers, didReview=didReview,
                           ratings=ratings, average_rating=average_rating, data=data
                           )
