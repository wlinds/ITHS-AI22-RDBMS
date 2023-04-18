import sqlite3
connection = sqlite3.connect('Explorations/test-db.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM dogs")
_ = cursor.fetchall()
for i in _:
    print(i)
    
connection.close()