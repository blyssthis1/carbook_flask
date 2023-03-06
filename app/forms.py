from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email


class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    email = StringField('Email:', validators =[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password:', validators=[DataRequired(), EqualTo('password',  message= "Password must match!")])
    first_name= StringField('First Name:', validators=[DataRequired()])
    last_name= StringField('Last Name:', validators=[DataRequired()])
    submit = SubmitField('Join!')

class SignInForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In!')

class ContactUsForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    phone = StringField('Phone number:', validators=[DataRequired()])
    body = TextAreaField("What's on your mind!", validators=[DataRequired()])
    submit = SubmitField('Submit!')

class CarInfoForm(FlaskForm):
    make = StringField('Make:', validators=[DataRequired()])
    model = StringField('Model:', validators=[DataRequired()])
    year = StringField('Year:', validators=[DataRequired()])
    color = StringField('Color:', validators=[DataRequired()])
    price = StringField('Price:', validators=[DataRequired()])
    submit = SubmitField('Submit!')
    