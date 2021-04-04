from flask_wtf import Form
from wtforms import TextField, PasswordField, TextAreaField
from wtforms.validators import Required, Email, EqualTo



class LoginForm(Form):
    username    = TextField('Username', [Required(message='Username Required')])
    password = PasswordField('Password', [Required(message='Password Required')])

class RegisterForm(Form):
    username = TextField('Username', [Required(message='Username Required')])
    password = PasswordField('Password', [Required(message='Password Required')])


# Admin Stuff
class AddGameForm(Form):
    title = TextField('Username', [Required(message='Username Required')])
    description = TextField('Description', [Required(message='Description Required')])