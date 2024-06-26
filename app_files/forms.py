from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Suggest')