from random import choices
from secrets import choice
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,DateField,DateTimeField,FileField, TextAreaField,SelectField,BooleanField,IntegerField,FloatField, SubmitField
from wtforms.validators import DataRequired,Email
from flask_wtf.file import FileField, FileAllowed, FileRequired
#choices
Year=['First Year','Second Year','Third Year','Fourth Year']
Dept=['Arch','CE','ECE','EE','EG','ICE','IT']



class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[Email()])
    role = SelectField('Role', validators=[DataRequired()])
    year = SelectField('Year' ,validators=[DataRequired()])
    dept = SelectField('Department', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[DataRequired()],id='password')
    check = BooleanField('Show password', id='check')
    submit = SubmitField('Login')


class BlogForm(FlaskForm):
    upload = FileField('Blog Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content')
    author = StringField('Author', validators=[DataRequired()])
    submit = SubmitField('Create Blog')


class GroundForm(FlaskForm):
    groundName = StringField('Ground Name', validators=[DataRequired()])
    NoOfCourt = IntegerField('No Of Court', validators=[DataRequired()])
    bookTime = FloatField('Game Duration(Hours)', validators=[DataRequired()])
    submit = SubmitField('Create')


class BookingForm(FlaskForm):
    groundName = SelectField('Ground', validators=[DataRequired()])
    team_1=SelectField('Team 1', validators=[DataRequired()])
    team_2=SelectField('Team 2', validators=[DataRequired()])
    courtName = SelectField('Court', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    time = SelectField('Time' ,validators=[DataRequired()])
    submit = SubmitField('Book Now')