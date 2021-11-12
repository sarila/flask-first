from flask import Flask,render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# configurtaion to connect to database
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'c4a7217c10e333af03e92501'
db = SQLAlchemy(app)

from market import routes