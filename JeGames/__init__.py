import urllib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

use_database="mysql" #mysql or mssql

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '/uploads'
app.db_type = 'mysql'

os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)



from JeGames import routes
