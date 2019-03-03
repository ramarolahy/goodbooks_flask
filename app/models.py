from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Book(db.Model):
    """
    Create a Book table
    """
    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(60), index=True, unique=True, nullable=False)
    title = db.Column(db.String(60), index=True, nullable=False)
    author = db.Column(db.String(60), index=True, nullable=False)
    year = db.Column(db.String(4), nullable=False)
    user_reviews = db.relationship('Review', backref='book', lazy='dynamic')


    def __repr__(self):
        return '<Book: {}>'.format(self.isbn)


class Review(db.Model):
    """
    Create a Review table
    """
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    review_date = db.Column(db.DateTime, nullable=False)
    book_isbn = db.Column(db.String(60), db.ForeignKey('books.isbn'), index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    rating = db.Column(db.String(1), nullable=False)
    review_text = db.Column(db.String(), nullable=False)
    users = db.relationship('User', backref='review', lazy=True)

    def __repr__(self):
        return '<Review: {}>'.format(self.book_isbn)


class User(UserMixin, db.Model):
    """
    Create an User table

    UserMixin provides default implementations for the methods that Flask-Login
    expects user objects to have.
    see https://flask-login.readthedocs.io/en/latest/#flask_login.UserMixin
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    books_reviewed = db.relationship('Review', backref='user', lazy=True)

    @property
    def password(self):
        """
        PREVENT PASSWORD FROM BEING ACCESSED
        :return: Error Message
        """
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        HASH USER PASSWORD
        :param password: User password
        :return: hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        CHECK IF HASHED PASSWORD MATCHES USER PASSWORD
        :param password:
        :return: boolean
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.email)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))