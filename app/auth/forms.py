from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Reader

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    wtforms will create the forms
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    # Check if email is already in use first
    # USE SQL COMMANDS FOR QUERY
    def validate_email(self, field):
        if Reader.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    wtforms will create the forms
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

