import database

# Add single record to table
database.add_one("Ring", 300, 50)


# Delete record id must be passed as string
database.delete_product('2')

# Add many record at once
new_records = [
('Laptop', 150000, 5),
('Jacket', 2000, 10)
]
database.add_many(new_records)

# lookup using where clause
database.product_lookup("Watch")

# Show all data
database.show_all()

