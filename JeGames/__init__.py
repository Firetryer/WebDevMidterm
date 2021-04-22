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
app.config['SECRET_KEY'] = SECRET_KEY
app.config['CSRF_ENABLED'] = True
app.config['CSRF_SESSION_KEY'] = SECRET_KEY
if 'IS_HEROKU' in os.environ:
    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["db_uri"]



os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'

csrf = CSRFProtect(app)
csrf.init_app(app)

from JeGames import routes
from JeGames.models import AppUser, Game
migrate = Migrate(app, db)
