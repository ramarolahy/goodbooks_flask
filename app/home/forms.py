from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired


class BookSearchForm(FlaskForm):
    """
    Form to search for a book
    """
    choices = [
        ('isbn', 'ISBN'),
        ('author', 'Author'),
        ('title', 'Title')
    ]
    select = SelectField('Search for a book:&nbsp;&nbsp;&nbsp;',
                         choices=[('title', 'By Title'), ('author', 'By Author'), ('isbn', 'By ISBN')])
    search = StringField('', validators=[DataRequired()])
    submit = SubmitField('Search')

class ReviewForm(FlaskForm):
    """
    Form to submit review
    """
    rating = SelectField('Select your rating:&nbsp;&nbsp;&nbsp;',
                        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])
    review = TextAreaField('Enter your review', validators=[DataRequired()])
    submit = SubmitField('Submit Review')