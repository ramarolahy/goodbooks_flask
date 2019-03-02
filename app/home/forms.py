from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class BookSearchForm(FlaskForm):
    """
    Form to search for a book
    """
    choices = [
        ('ISBN', 'ISBN'),
        ('Author', 'Author'),
        ('Title', 'Title')
    ]
    select = SelectField('Search for a book:   ', choices=choices)
    search = StringField('', validators=[DataRequired()])
    submit = SubmitField('Search')