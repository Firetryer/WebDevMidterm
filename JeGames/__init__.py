import urllib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from werkzeug.utils import secure_filename
import os

use_database="mysql" #mysql or mssql

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '/uploads'
app.db_type = 'mysql'

os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'



from JeGames import routes
