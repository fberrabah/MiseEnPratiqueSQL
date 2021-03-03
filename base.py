import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="FARIDZ",
  password="Password08-",
  database="AGENCE2"
)

#mycursor.execute("CREATE TABLE CITY (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, distance INT NOT NULL, people INT NOT NULL, PRIMARY KEY (id))")

mycursor = mydb.cursor()

mycursor.execute("describe CITY")

for x in mycursor:
  print(x)
