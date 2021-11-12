from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm
from market import db

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


@app.route('/register', methods=['GET', 'POST']) #to handle different HTTP request
def register_page():
	form = RegisterForm()
	# if form is submited do this
	if form.validate_on_submit():
		user_to_create = User(username=form.username.data,
			email_address=form.email_address.data,
			password_hash=form.password1.data)
		db.session.add(user_to_create)
		db.session.commit()
		return redirect(url_for('market'))
	if form.errors != {}: #If no errors from validations
		for err_msg in form.errors.values():
			flash(f'There was error creating user: {err_msg}', category='danger')

	return render_template('register.html', form=form)
