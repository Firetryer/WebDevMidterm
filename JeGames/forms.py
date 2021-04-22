from flask_wtf import Form
from wtforms import TextField, PasswordField, TextAreaField
from wtforms.validators import Required, Email, EqualTo


class LoginForm(Form):
    username    = TextField('Username', [Required(message='Username Required')])
    password = PasswordField('Password', [Required(message='Password Required')])

class RegisterForm(Form):
    username = TextField('Username', [Required(message='Username Required')])
    email = TextField('Email', [Required(message='Username Required'), Email(message="Valid Email required")])
    password = PasswordField('Password', [Required(message='Password Required'), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', [Required(message='Password Required')])


# Admin Stuff
class AddGameForm(Form):
    title = TextField('Username', [Required(message='Username Required')])
    description = TextField('Description', [Required(message='Description Required')])