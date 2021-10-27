from flask import Flask,render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# configurtaion to connect to database
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///market.db'

db = SQLAlchemy(app)

from market import routes