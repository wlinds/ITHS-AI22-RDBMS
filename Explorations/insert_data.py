import sqlite3
connection = sqlite3.connect('Explorations/test-db.db')
cursor = connection.cursor()

dogs = [['Piff', 'Dalmatiner', 3, '2019-10-21'],
          ['Uffe', 'Schapendoes', 13, '2011-03-04'],
          ['Spik', 'Prague ratter', 6, '2017-02-10'],
          ['Puff', 'Dalmatiner', 3, '2019-10-21']]

for i in range(len(dogs)):
    dog_name = dogs[i][0]
    dog_breed = dogs[i][1]
    age = dogs[i][2]
    birthday = dogs[i][3]
    cursor.execute("INSERT INTO dogs VALUES (?, ?, ?, ?)", (dog_name, dog_breed, age, birthday))

connection.commit()
connection.close()