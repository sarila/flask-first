from market import db

# Model of a table
class Item(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(length=20), nullable=True, unique=True)
	price = db.Column(db.Integer(), nullable=False, unique=True)
	barcode = db.Column(db.String(length=12), nullable=False, unique=True)
	description = db.Column(db.String(length=2000) )

	def __repr__(self):
		return f'Item {self.name}'
