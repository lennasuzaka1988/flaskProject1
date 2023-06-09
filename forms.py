from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, DataRequired, Email
import email_validator


class ContactForm(FlaskForm):
    name = StringField(label='Name: ', validators=[DataRequired()])
    email = StringField(label='Email: ', validators=[DataRequired(), Email(granular_message=True)])
    message = TextAreaField(label='Message: ')
    subject = StringField(label='Subject: ')
    submit = SubmitField(label='Send Message')


# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[InputRequired(),
#                                              Length(min=10, max=30)])
#     password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=16)])