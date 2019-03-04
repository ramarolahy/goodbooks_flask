
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from datetime import timedelta

from .forms import LoginForm, RegistrationForm
from ..models import Reader
from . import auth
from .. import db


# Register route
# ===============================================
@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add aa user to the database through the registration form
    """

    #
    form = RegistrationForm()
    if form.validate_on_submit():
        reader = Reader(email=form.email.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    password=form.password.data)

        # add reader to the database
        db.session.add(reader)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register', active='register')


# Login route
# ===============================================
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log a reader in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether reader exists in the database and whether
        # the password entered matches the password in the database
        reader = Reader.query.filter_by(email=form.email.data).first()
        if reader is not None and reader.verify_password(
                form.password.data):
            # Login and validate the reader.
            # reader should be an instance of your `User` class
            login_user(reader, remember=True, duration=timedelta(seconds=1800))

            # redirect to the profile page after login
            return redirect(url_for('home.profile', reader=reader.first_name ))

        # when login details are incorrect
        else:
            flash('Invalid email or password.', 'error')

    # load login template
    return render_template('auth/login.html', form=form, title='Login', active='login')


# Logout route
# ===============================================
@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an reader out through the logout link
    """
    logout_user()

    # redirect to the login page
    return redirect(url_for('auth.login'))
