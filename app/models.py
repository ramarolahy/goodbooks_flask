import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = "postgres://btetampwgolbgl: 4fdc0ef18ff204c01816a6677422c6ef4f44771fae9518aeae8ae9b40e8839f3" \
               " @ ec2 - 107 - 20 - 185 - 27.compute - 1.amazonaws.com: 5432 / d7jkbrbmpshg7n"

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

