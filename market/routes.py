from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm

# route decorater
@app.route('/')
@app.route('/home')
def home_page():
	return render_template('home.html')

@app.route('/about-us')
def about_us():
	return render_template('about.html')

@app.route('/market')
def market():
	items = Item.query.all()
	return render_template('market.html', items=items)

@app.route('/upload')
def upload():
	return render_template('upload.html')


@app.route('/register')
def register_page():
	form = RegisterForm()
	return render_template('register.html', form=form)
