from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import case, func, select
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from flask_bcrypt import Bcrypt
from JeGames import db, login_manager
from flask_login import UserMixin
from datetime import datetime
import decimal



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


#= Models
class AppUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.LargeBinary(90), unique=False, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    admin = db.Column(db.Boolean(), unique=False, nullable=False)
    register_date = db.Column(db.DateTime(), nullable=False)
    owned_games = db.relationship("Game", secondary = owned_games)
    reviews = db.relationship("Review", backref="users")

    def reviewed_game(self, game_id):
        if game_id in [review.game_id for review in self.reviews]:
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=False, nullable=False)
    description = db.Column(db.Text(), unique=False, nullable=True)
    discount = db.Column(db.Integer, unique=False, nullable=True)
    discount_end_date = db.Column(db.DateTime(), nullable=True)
    discount_start_date = db.Column(db.DateTime(), nullable=True)
    discount_expirable = db.Column(db.Boolean, unique=False, nullable=True)
    price = db.Column(db.Numeric(38, 2), unique=False, nullable=True)
    developer = db.Column(db.String(60), unique=False, nullable=True)
    publisher = db.Column(db.String(60), unique=False, nullable=True)
    status = db.Column(db.String(30), unique=False, nullable=True)
    features = db.Column(db.Text(), unique=False, nullable=True)
    other_details = db.Column(db.Text(), unique=False, nullable=True)
    languages = db.Column(db.String(160), unique = False, nullable=True)
    image_main = db.Column(db.String(120), unique=False, nullable=True)
    image_banner = db.Column(db.String(120), unique=False, nullable=True)
    platforms = db.relationship("Platform", backref="games", lazy='dynamic')
    tags = db.relationship("Tag", backref = "games", secondary = game_tag)
    reviews = db.relationship("Review", backref="games")

    @hybrid_property
    def rating(self):
        return sum([review.rating for review in self.reviews])

    @rating.expression
    def rating(cls):
        return (
            select([func.sum(Review.rating)]).
            where(Review.game_id == cls.id)
        )

    @hybrid_property
    def has_discount(self):
        if self.discount > 0:
            if self.discount_expirable == True:
                if self.discount_end_date != None:
                    if self.discount_end_date < datetime.now():
                        return False
                    else:
                        return True
                else:
                    return False
            else:
                return True
        return False

    @has_discount.expression
    def has_discount(cls):
        return case(
            [
                ((cls.discount > 0) & (cls.discount_expirable == False), True),
                ((cls.discount > 0) & (cls.discount_expirable == True) & (cls.discount_end_date > datetime.now()), True)], else_=False)

    @hybrid_property
    def discount_price(self):
        if self.discount > 0:
            if self.discount_expirable == True:
                if self.discount_end_date != None:
                    if self.discount_end_date < datetime.now():
                        return self.price
        return (self.price - (self.price * decimal.Decimal(self.discount / 100))).quantize(decimal.Decimal('.01'), decimal.ROUND_HALF_UP)

    @discount_price.expression
    def discount_price(cls):
        discount = cls.price - (cls.price * cls.discount / 100)
        return case([((cls.discount > 0) & (cls.discount_expirable == True) & (cls.discount_end_date < datetime.now()), cls.price)],else_=discount)
    



class Review(db.Model):
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('app_user.id'), primary_key = True)
    review_title = db.Column(db.String(60), unique=False, nullable=False)
    review_text = db.Column(db.String(4000), unique=False, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)
    date_published = db.Column(db.DateTime(), nullable=False)


class Platform(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    available = db.Column(db.Boolean, unique=False, nullable=True)
    name = db.Column(db.String(60), unique=False, nullable=True)
    min_os = db.Column(db.String(60), unique = False, nullable=True)
    min_processor = db.Column(db.String(60), unique = False, nullable=True)
    min_memory = db.Column(db.String(60), unique = False, nullable=True)
    min_storage = db.Column(db.String(60), unique = False, nullable=True)
    min_graphics = db.Column(db.String(60), unique = False, nullable=True)
    max_os = db.Column(db.String(60), unique = False, nullable=True)
    max_processor = db.Column(db.String(60), unique = False, nullable=True)
    max_memory = db.Column(db.String(60), unique = False, nullable=True)
    max_storage = db.Column(db.String(60), unique = False, nullable=True)
    max_graphics = db.Column(db.String(60), unique = False, nullable=True)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True, nullable = False)


class WebsiteSetting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    setting_name = db.Column(db.String(32), unique=True, nullable=False)
    setting_value = db.Column(db.String(32), unique=False, nullable=True)
    setting_group = db.Column(db.String(32), unique=False, nullable=True)