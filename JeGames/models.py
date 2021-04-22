from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from JeGames import db

# Helpers
def create_account(username, password):
	hashed_password = bcrypt.generate_password_hash(password)
	new_account = User(username=username, password=hashed_password)
	db.session.add(new_account)
	db.session.commit()

# Models
class AppUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.LargeBinary(90), unique=False, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    admin = db.Column(db.Boolean(), unique=False, nullable=False)
    register_date = db.Column(db.DateTime(), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=False, nullable=False)
    description = db.Column(db.Text(), unique=False, nullable=False)
    discount = db.Column(db.Numeric(2, 2), unique=False, nullable=False)
    price = db.Column(db.Numeric(2, 2), unique=False, nullable=False)
    
