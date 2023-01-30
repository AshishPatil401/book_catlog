
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


class RegistrationForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired(), Length(2,20, message="Name should be at least 2 characters and less than 20 characters")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(5), EqualTo('confirm', 'Password must match.')])
    confirm = PasswordField('Confirm')
    submit = SubmitField('Register')

    

