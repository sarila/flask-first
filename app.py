from flask import Flask,render_template, redirect, url_for
app = Flask(__name__)

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
	items = [
	    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
	    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
	    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
	]
	return render_template('market.html', items=items)

@app.route('/upload')
def upload():
	return render_template('upload.html')