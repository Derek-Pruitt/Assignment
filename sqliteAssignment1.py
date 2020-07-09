

import sqlite3
# get user personal info and insert into a tuple
firstName = input("Enter your name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName,lastName,age)

with sqlite3.connect('Test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?,?,?)",personData)

c.execute("UPDATE People SET age=? Where firstName=? AND lastName=?",
          (42,'RO','Obvious'))

    
