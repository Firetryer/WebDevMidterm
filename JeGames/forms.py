from flask_wtf import Form
from flask_wtf.file import FileField
from wtforms import widgets, TextField, PasswordField, TextAreaField, DecimalField, BooleanField, SelectField, IntegerField, DateTimeField, FieldList, FormField, HiddenField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import Required, Email, EqualTo, ValidationError, NumberRange
from JeGames.models import AppUser, Tag, Game, game_tag
from JeGames import db


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



class TagField(Form):
    tag = BooleanField()

# Admin Stuff
class AddGameForm(Form):
    def __init__(self, game_id, *args, **kwargs):
        super(AddGameForm, self).__init__(*args, **kwargs)
        self.game_id = game_id

    title = TextField('Username', [Required(message='Title Required')])
    description = TextAreaField('Description', [Required(message='Description Required')])
    price = DecimalField('Price',[
        Required(message='A Price is required')
    ], places=2)

    discount = IntegerField("Discount", [NumberRange(min = 0, max = 100, message = "Discount must be between 0-100")])
    discount_expirable = BooleanField("Expirable")
    discount_end_date = DateTimeField("End Date")
    discount_start_date = DateTimeField("Start Date")

    developer = TextField('Developer')
    publisher = TextField('Publisher')
    status = SelectField(u'Field name', choices = ["coming soon", "available"])
    features = TextAreaField('Features')
    other_details = TextAreaField('Other Details')
    languages = TextAreaField('Languages')
    image_main = FileField("Main Image")
    image_banner = FileField("Banner Image")

    win_available = BooleanField("Available")
    win_min_os = TextField('Minimum OS')
    win_min_processor = TextField('Minimum Processor')
    win_min_memory = TextField('Minimum Memory')
    win_min_storage = TextField('Minimum Storage')
    win_min_graphics = TextField('Minimum Graphics')
    win_max_os = TextField('Recommended OS')
    win_max_processor = TextField('Recommended Processor')
    win_max_memory = TextField('Recommended Memory')
    win_max_storage = TextField('Recommended Storage')
    win_max_graphics = TextField('Recommended Graphics')

    linux_available = BooleanField("Available")
    linux_min_os = TextField('Minimum OS')
    linux_min_processor = TextField('Minimum Processor')
    linux_min_memory = TextField('Minimum Memory')
    linux_min_storage = TextField('Minimum Storage')
    linux_min_graphics = TextField('Minimum Graphics')
    linux_max_os = TextField('Recommended OS')
    linux_max_processor = TextField('Recommended Processor')
    linux_max_memory = TextField('Recommended Memory')
    linux_max_storage = TextField('Recommended Storage')
    linux_max_graphics = TextField('Recommended Graphics')

    mac_available = BooleanField("Available")
    mac_min_os = TextField('Minimum OS')
    mac_min_processor = TextField('Minimum Processor')
    mac_min_memory = TextField('Minimum Memory')
    mac_min_storage = TextField('Minimum Storage')
    mac_min_graphics = TextField('Minimum Graphics')
    mac_max_os = TextField('Recommended OS')
    mac_max_processor = TextField('Recommended Processor')
    mac_max_memory = TextField('Recommended Memory')
    mac_max_storage = TextField('Recommended Storage')
    mac_max_graphics = TextField('Recommended Graphics')

    tags = QuerySelectMultipleField(
        'Tag',
        query_factory = lambda: Tag.query.all(),
        widget = widgets.ListWidget(html_tag="ol", prefix_label=False),
        option_widget = widgets.CheckboxInput(),
        get_label='title',
        default = lambda: Tag.query.join(game_tag).filter(Tag.id == game_tag.c.tag_id).all()
        #default = lambda a: db.session.query(game_tag).filter(game_tag.c.tag_id==a).one()
    )

class SetFeaturedForm(Form):
    f1 = IntegerField("Featured 1")
    f2 = IntegerField("Featured 2")
    f3 = IntegerField("Featured 3")
    f4 = IntegerField("Featured 4")
    f5 = IntegerField("Featured 5")


class AddTagForm(Form):
    title = TextField('title', [
        Required(message='Field Required'),
        Unique(Tag, Tag.title, "Tag already exists")])