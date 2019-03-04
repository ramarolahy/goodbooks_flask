from flask import Blueprint

"""
The Auth blueprint will handle all authentication pages (registration and login)
"""
# auth Blueprint constructor
auth = Blueprint('auth', __name__)

# Must come after instantiation
from . import views

