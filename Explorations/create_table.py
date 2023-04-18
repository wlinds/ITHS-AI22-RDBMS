import sqlite3 # Create Table and DB in Python for SQL with sqlite3

connection = sqlite3.connect('Explorations/test-db.db')
cursor = connection.cursor()

# Each entry will have - name, breed, age, birthday (YYYY-MM-DD)

create_table_query = """
CREATE TABLE dogs (
dog_name VARCHAR(30),
dog_breed VARCHAR(30),
age INTEGER,
birthday DATE )"""
cursor.execute(create_table_query)
connection.commit()
connection.close()