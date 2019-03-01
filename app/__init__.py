
# Third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# from flask_session import Session

# local imports
from config import app_config

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

db = SQLAlchemy()

login_Manager = LoginManager()

# Initialize the app
def create_app(config_name):
    # instance_relative_config is the relative path to instance folder to the root
    # must be direct relative to app folder
    app = Flask(__name__, instance_relative_config=True)
    # Load the config file
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    login_Manager.init_app(app)
    login_Manager.login_message = "Please login to view this page"
    login_Manager.login_view = "auth.login"

    # Configure session to use filesystem
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    #db.init_app(app)
    #Session(app)



    return app






