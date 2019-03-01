from flask_login import UserMixin
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
    user_reviews = db.relationship('User', backref='book', lazy='dynamic')


    def __repr__(self):
        return '<Book: {}>'.format(self.isbn)



class User(UserMixin, db.Model):
    """
    Create an User table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    books_reviewed = db.Column(db.String(20), db.ForeignKey('books.isbn'))

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
        return '<User: {}>'.format(self.username)
