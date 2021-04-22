import urllib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import os



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/uploads'
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:F1retry3r@localhost/jegames"
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from JeGames import routes
from JeGames.models import User, Game
migrate = Migrate(app, db)
