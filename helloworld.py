from flask import Flask,render_template, redirect, url_for
app = Flask(__name__)

# route decorater
@app.route('/')
@app.route('/home')
def home_page():
	return render_template('home.html')

# string variable in url
@app.route('/hello/<name>')
def hello_name(name):
	return 'Hello ' + name

#Using URL_FOR (URL Building in Flask)

@app.route('/admin')
def hello_admin():
	return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
	return 'Hello ' + guest + '! You are logined as a guest' 

@app.route('/user/<name>')
def hello_user(name):
	if name=='admin':
		return redirect(url_for('hello_admin'))

	else:
		return redirect(url_for('hello_guest', guest=name))

if __name__ == '__main__':
	app.run(debug=True)