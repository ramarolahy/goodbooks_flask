# Third party imports
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# Local imports
from app import db, login_Manager


class Book(db.Model):
    """
    CREATE A BOOKS TABLE
    """
    __tablename__ = "books"

    isbn = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    reviews = db.relationship("Users", backref="books", lazy=True)


class User(UserMixin, db.Model):
    """
    CREATE AN EMPLOYEE TABLE
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(55), index=True, unique=True, nullable=False)
    username = db.Column(db.String(30), index=True, unique=True, nullable=False)
    first_name = db.Column(db.String(30), index=True, nullable=False)
    last_name = db.Column(db.String(30), index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    books_reviewed = db.Column(db.Integer, db.ForeignKey('books.isbn'), unique=True)

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

