import urllib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from werkzeug.utils import secure_filename
import os

use_database="mysql" #mysql or mssql

app = Flask(__name__)
app.config["SECRET_KEY"] = 'f5418130a27f18abe557d61201c31d60'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://rewelcabiles:1539274@localhost/LoggingSystem'
app.config['UPLOAD_FOLDER'] = '/uploads'
app.db_type = 'mysql'

os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'



from LoggingSystem import routes
