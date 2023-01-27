
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, email, ValidationError


class RegistrationForm(FlaskForm):

    name = StringField('Name')
    email = StringField('Email', validators=[DataRequired(), email()])
    password = PasswordField('Password')
    confirm = PasswordField('Confirm')
    submit = SubmitField('Register')

    

