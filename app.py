from flask import Flask,render_template, redirect, url_for
app = Flask(__name__)

# route decorater
@app.route('/')
@app.route('/home')
def home_page():
	return render_template('home.html')

@app.route('/aboutus')
def about_us():
	return render_template('about.html')

@app.route('/market')
def market():
	return render_template('market.html')

@app.route('/upload')
def upload():
	return render_template('upload.html')