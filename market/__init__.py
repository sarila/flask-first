from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# configurtaion to connect to database
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'c4a7217c10e333af03e92501'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from market import routes