from flask_wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, DecimalField
from wtforms.validators import Required, Email, EqualTo, ValidationError
from JeGames.models import AppUser


class Unique(object):
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'this element already exists'
        self.message = message
        
    def __call__(self, form, field):
        if field.object_data == field.data:
            return
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

class LoginForm(Form):
    username = TextField('Username', [Required(message='Username Required')])
    password = PasswordField('Password', [Required(message='Password Required')])

class RegisterForm(Form):
    username = TextField('Username', [
        Required(message='Username Required'),
        Unique(AppUser, AppUser.username, "Username taken")])
    email = TextField('Email', [
        Required(message='Email Required'),
        Email(message="Valid Email required"),
        Unique(AppUser, AppUser.email, "Email already in use")])
    password = PasswordField('Password', [
        Required(message='Password Required'),
        EqualTo('confirm_password',
        message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', [Required(message='Password Required')])


# Admin Stuff
class AddGameForm(Form):
    title = TextField('Username', [Required(message='Title Required')])
    description = TextAreaField('Description', [Required(message='Description Required')])
    price = DecimalField('Price',[
        Required(message='A Price is required')
    ], places=2)
    developer = TextField('Developer')
    publisher = TextField('Publisher')
    status = TextField('Status')
    rating = DecimalField('Rating')
    features = TextAreaField('Features')
    other_details = TextAreaField('Other Details')
    languages = TextAreaField('Languages')

