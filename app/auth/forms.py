
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.auth.models import User



def eamil_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError("Email already exists...!!!")



class RegistrationForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired(), Length(2,20, message="Name should be at least 2 characters and less than 20 characters")])
    email = StringField('Email', validators=[DataRequired(), Email(), eamil_exists])
    password = PasswordField('Password', validators=[DataRequired(), Length(5), EqualTo('confirm', 'Password must match.')])
    confirm = PasswordField('Confirm')
    submit = SubmitField('Register')



class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('stay_loggedin')
    submit = SubmitField('LogIn')
    

