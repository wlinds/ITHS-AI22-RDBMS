import sqlite3
connection = sqlite3.connect('Explorations/primes.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM numbers")
_ = cursor.fetchall()
for i in _:
    print(i)
    
connection.close()