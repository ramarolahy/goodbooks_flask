from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

"""
    Association table for User and Book
    
    User and Book has a Many-To-Many relationship
        One Book can have Many Reader 
        One User can have Many Book
"""
association_table = db.Table('association',
                        db.Column('reader_id', db.Integer, db.ForeignKey('readers.id')),
                        db.Column('book_id', db.Integer, db.ForeignKey('books.id'))
                             )

class Reader(UserMixin, db.Model):
    """
    Create an User table

    UserMixin provides default implementations for the methods that Flask-Login
    expects user objects to have.
    see https://flask-login.readthedocs.io/en/latest/#flask_login.UserMixin
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'readers'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    reviews = db.relationship('Review', backref='reader', lazy=True)
    books_reviewed = db.relationship('Book', secondary=association_table, back_populates='readers')

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
        return '<Reader: '+ self.first_name + ' ' + self.last_name


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Reader.query.get(int(user_id))


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
    reviews = db.relationship('Review', backref='book', lazy='dynamic')
    readers = db.relationship('Reader', secondary=association_table, back_populates='books_reviewed')




    def __repr__(self):
        return '<Book: >'+ self.title + ' by ' + self.author


class Review(db.Model):
    """
    Create a Review table

    Review has One-To-Many relationship to User and Book
        One Review can only have ONE User and One Book
        Each Book can have MANY Review
        Each User can submit Many Review
    """
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    review_date = db.Column(db.DateTime, nullable=False)
    rating = db.Column(db.String(1), nullable=False)
    review_title = db.Column(db.String(), nullable=True)
    review_text = db.Column(db.String(), nullable=False)
    book_isbn = db.Column(db.String(60), db.ForeignKey('books.isbn'), index=True, nullable=False)
    reader_id = db.Column(db.Integer, db.ForeignKey('readers.id'), unique=True, nullable=False)


    def __repr__(self):
        return '<Review: >'+ self.review_title
