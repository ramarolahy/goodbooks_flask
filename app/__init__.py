# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    # Create and initialize Flask app
    # config.py is locate with instance_relative_config
    app = Flask(__name__, instance_relative_config=True)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # Create  and initialize LoginManager object
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    # Migration will allow to make changes to the models in the future
    # run flask db migrate THEN run flask db upgrade AFTER making changes
    migrate = Migrate(app, db)

    # Register the blueprints
    # I will use blueprints for the sake of practicine
    # To learn more about blueprints, see http://flask.pocoo.org/docs/1.0/blueprints/
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)


    return app