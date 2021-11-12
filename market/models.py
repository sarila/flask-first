from market import db
from market import Bcrypt

# User table
class User(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(length=30), nullable=False, unique=True)
	email_address = db.Column(db.String(length=50), nullable=False, unique=True)
	password_hash = db.Column(db.String(length=60), nullable=False)
	budget = db.Column(db.Integer(), nullable=False, default=1000)
	# Relationship between user and items defined
	items = db.relationship('Item', backref="owned_user", lazy=True)


	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, plain_text_password):
		self.password_hash = Bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
	
# Model of a table
class Item(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(length=20), nullable=True, unique=True)
	price = db.Column(db.Integer(), nullable=False, unique=True)
	barcode = db.Column(db.String(length=12), nullable=False, unique=True)
	description = db.Column(db.String(length=2000), nullable=False)
	owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

	def __repr__(self):
		return f'Item {self.name}'
