import sqlite3

# Connect to database
# conn = sqlite3.connect('product.db')

# Cursor for db
# c = conn.cursor()

# Create Tables
#Null, integer, real, text, blob
# c.execute(""" CREATE TABLE products (
# 		product_name TEXT,
# 		price REAL,
# 		quantity INTEGER
# 	) """)

# conn.commit()
# print("Table Created Successfully")

# Query to return all data
def show_all():
	# Connect to database
	conn = sqlite3.connect('product.db')

	# Cursor for db
	c = conn.cursor()
	c.execute("SELECT rowid, * FROM products")
	items = c.fetchall()

	for item in items:
		print(item)

	# commit the command
	conn.commit()

	# Close the connection
	conn.close()


# Add a Data in the database
def add_one(name, price, quantity):
	# Connect to database
	conn = sqlite3.connect('product.db')

	# Cursor for db
	c = conn.cursor()
	c.execute("INSERT INTO products VALUES (?,?,?)", (name, price, quantity))


	# commit the command
	conn.commit()
	print("Product Added Successfully")

	# Close the connection
	conn.close()

def delete_product(id):
	# Connect to database
	conn = sqlite3.connect('product.db')

	# Cursor for db
	c = conn.cursor()
	c.execute("DELETE FROM products WHERE rowid = (?)", id)
	conn.commit()
	print("Product Deleted Successfully")
	conn.close()

# Add many record at once
def add_many(list):
	conn = sqlite3.connect('product.db')
	c = conn.cursor()
	c.executemany("INSERT INTO products VALUES (?,?,?)", (list))

	# commit the command
	conn.commit()
	print("Product(s) Added Successfully")

	# Close the connection
	conn.close()


# Lookup Products
def product_lookup(name):
	conn = sqlite3.connect('product.db')
	c = conn.cursor()
	c.execute("SELECT rowid, * FROM products WHERE product_name = (?)", (name,))
	items = c.fetchall()

	for item in items:
		print(item)

	# commit the command
	conn.commit()
	# Close the connection
	conn.close()