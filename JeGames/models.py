from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from JeGames import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return AppUser.query.get(user_id)


# Helpers
def create_account(username, password):
    hashed_password = bcrypt.generate_password_hash(password)
    new_account = User(username=username, password=hashed_password)
    db.session.add(new_account)
    db.session.commit()

####=== Tables

#= Relationship/Association Tables
owned_games = db.Table('owned_games', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('app_user.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'))
)

game_tag = db.Table('game_tag', db.Model.metadata,
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'))
)

game_platform = db.Table('game_platform', db.Model.metadata,
    db.Column('game_id', db.Integer, db.ForeignKey('game.id')),
    db.Column('platform_id', db.Integer, db.ForeignKey('platform.id'))
)

#= Models
class AppUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.LargeBinary(90), unique=False, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    admin = db.Column(db.Boolean(), unique=False, nullable=False)
    register_date = db.Column(db.DateTime(), nullable=False)
    owned_games = db.relationship("Game", secondary = owned_games)
    reviews = db.relationship("Review", backref="app_user", lazy='dynamic')
    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=False, nullable=False)
    description = db.Column(db.Text(), unique=False, nullable=False)
    discount = db.Column(db.Numeric(2, 2), unique=False, nullable=False)
    price = db.Column(db.Numeric(2, 2), unique=False, nullable=False)
    developer = db.Column(db.String(60), unique=False, nullable=False)
    publisher = db.Column(db.String(60), unique=False, nullable=False)
    status = db.Column(db.String(30), unique=False, nullable=False)
    rating = db.Column(db.Numeric(2, 1), unique=False, nullable=False)
    features = db.Column(db.Text(), unique=False, nullable=False)
    other_details = db.Column(db.Text(), unique=False, nullable=False)
    min_os = db.Column(db.String(60), unique = False, nullable=False)
    min_processor = db.Column(db.String(60), unique = False, nullable=False)
    min_memory = db.Column(db.String(60), unique = False, nullable=False)
    min_storage = db.Column(db.String(60), unique = False, nullable=False)
    min_graphics = db.Column(db.String(60), unique = False, nullable=False)
    max_os = db.Column(db.String(60), unique = False, nullable=False)
    max_processor = db.Column(db.String(60), unique = False, nullable=False)
    max_memory = db.Column(db.String(60), unique = False, nullable=False)
    max_storage = db.Column(db.String(60), unique = False, nullable=False)
    max_graphics = db.Column(db.String(60), unique = False, nullable=False)
    languages = db.Column(db.String(60), unique = False, nullable=False)
    platform = db.relationship("platform", secondary = game_platform)
    tags = db.relationship("Tag", secondary = game_tag)
    reviews = db.relationship("Review", backref="game", lazy='dynamic')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('app_user.id'))
    review_title = db.Column(db.String(60), unique=False, nullable=False)
    review_text = db.Column(db.String(4000), unique=False, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)
    date_published = db.Column(db.DateTime(), nullable=False)


class Platform(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True, nullable = False)
    