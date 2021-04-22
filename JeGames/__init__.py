import urllib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_wtf import CSRFProtect

import os



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/uploads'
if 'IS_HEROKU' in os.environ:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["db_uri"]
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
CSRFProtect(app)

from JeGames import routes
from JeGames.models import User, Game
migrate = Migrate(app, db)
