import urllib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_wtf import CSRFProtect
from flask_login import LoginManager

import os
import re



SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/uploads'
app.config['SECRET_KEY'] = b'\xd5[\x01"\x96aF@#\x94\xc9"\xc3\xc43(7\xe8\x9f]\xd5\x9f\x17 \xff\xa3$\x18D\xfa\x95\xae'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
if 'IS_HEROKU' in os.environ:
    uri = os.getenv("DATABASE_URL") 
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["db_uri"]



os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'flash_success'

csrf = CSRFProtect(app)

from JeGames import routes
from JeGames.models import AppUser, Game
migrate = Migrate(app, db, compare_type=True)
