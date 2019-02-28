import os
# Third party imports
from flask import Flask, session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# from flask_session import Session

# local imports
from config import app_config

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Initialize the app
def create_app(config_name):
    # instance_relative_config is the relative path to instance folder to the root
    # must be direct relative to app folder
    app = Flask(__name__, instance_relative_config=True)
    # Load the config file
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # Configure session to use filesystem
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    #db.init_app(app)
    #Session(app)

    @app.route('/')
    def books():
        return 'Books are nice!!'

    return app









# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

