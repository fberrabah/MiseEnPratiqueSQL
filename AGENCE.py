import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="FARIDZ",
  password="******",
  database="AGENCE2"
)
mycursor = mydb.cursor()


"""CREATE TABLE"""

#mycursor.execute("CREATE TABLE CITY (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, distance INT NOT NULL, people INT NOT NULL, PRIMARY KEY (id))")
#mycursor.execute("CREATE TABLE STYLE (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, base_rent INT NOT NULL, PRIMARY KEY (id))")
#mycursor.execute("CREATE TABLE DISTRICT (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL,city_id INT, PRIMARY KEY (id),CONSTRAINT FK_CityId FOREIGN KEY (city_id) REFERENCES CITY(id))")
#mycursor.execute("CREATE TABLE PLACE (id INT NOT NULL AUTO_INCREMENT, style VARCHAR(50) NOT NULL,street VARCHAR(50) NOT NULL,postale_code CHAR(99) NOT NULL,rent INT NOT NULL,area FLOAT,city_id INT,disctrict_id INT, PRIMARY KEY (id),CONSTRAINT FK_City_Id FOREIGN KEY (city_id) REFERENCES CITY(id),CONSTRAINT FK_District_Id FOREIGN KEY (disctrict_id) REFERENCES DISTRICT(id))")
#mycursor.execute("CREATE TABLE CLIENT (id INT NOT NULL AUTO_INCREMENT, first_name VARCHAR(255) NOT NULL, name VARCHAR(50), birthday DATE NOT NULL, phone VARCHAR(50) NOT NULL, PRIMARY KEY (id))")
#mycursor.execute("CREATE TABLE CONTRACT (id INT NOT NULL AUTO_INCREMENT,  contractday DATE NOT NULL,client_id INT,place_id INT, PRIMARY KEY (id),CONSTRAINT FK_Client_Id FOREIGN KEY (client_id) REFERENCES CLIENT(id),CONSTRAINT FK_Place_Id FOREIGN KEY (place_id) REFERENCES PLACE(id))")

""" add information in table """ 

# sql = "INSERT INTO CITY (name, distance, people) VALUES (%s, %s, %s)"
# val = [
#   ("LILLE", 8754, 4000),
#   ("Paris", 904, 800),
#   ("NEW YORK", 951, 15800),
#   ("BALI", 3574, 100),
#   ("MADRID", 258, 4484)
# ]
#mycursor.executemany(sql, val)

# sql = "INSERT INTO  CLIENT (first_name, name, birthday, phone) VALUES (%s, %s, %s, %s)"
# val = [
#   ("farid", "B", "1989/08/14", "03.20.20.20.20"),
#   ("pierre", "B","1989/08/14", "03.20.20.20.20"),
#   ("paule", "B","1989/08/14", "03.20.20.20.20"),
#   ("jacque", "B","1989/08/14","03.20.20.20.20"),
#   ("jean", "B","1989/08/14", "03.20.20.20.20")
#   ]

# mycursor.executemany(sql, val)

# sql = "INSERT INTO DISTRICT (name, city_id) VALUES (%s, %s)"
# val = [
#   ("saint pierre", 6),
#   ("barbes", 7),
#   ("bronx", 8),
#   ("thai", 9),
#   ("hala", 10),
#   ]

# mycursor.executemany(sql, val)


# sql = "INSERT INTO PLACE (style, street, postale_code, rent, area, city_id, disctrict_id) VALUES (%s, %s, %s, %s, %s ,%s , %s)"
# val = [
#   ("F1", "35 RUE A", "59290", 100, 320, 10, 10),
#   ("F2", "36 RUE B","59100", 200, 330, 6, 6),
#   ("F3", "37 RUE C","59000", 300, 340, 7, 7),
#   ("F4", "38 RUE D","59200", 400, 350, 8, 8),
#   ("F5", "39 RUE E","59300", 500, 360, 9, 9)
#   ]

# mycursor.executemany(sql, val)


# sql = "INSERT INTO CONTRACT (contractday, client_id, place_id) VALUES (%s, %s, %s)"
# val = [
#   ("2021/03/03", 1, 11),
#   ("2021/03/03", 2, 12),
#   ("2021/03/03", 3, 13),
#   ("2021/03/03", 4, 14),
#   ("2021/03/03", 5, 15)
#   ]

# mycursor.executemany(sql, val)

# sql = "INSERT INTO STYLE (name, base_rent) VALUES (%s, %s)"
# val = [
#   ("f1", 1),
#   ("f2", 2),
#   ("f3", 3),
#   ("f4", 4),
#   ("f5", 5)
#   ]

# mycursor.executemany(sql, val)




""" CHANGE INFORMATION IN TABLE """

# sql = "UPDATE CITY SET name = 'PARIS' WHERE name = 'Paris'"

# mycursor.execute(sql)

# mydb.commit()

# sql = "UPDATE CLIENT SET first_name = 'JEAN' WHERE first_name = 'jean'"

#mycursor.execute(sql)

#mydb.commit()

# sql = "UPDATE DISTRICT SET name = 'SAINT PIERRE' WHERE name = 'saint pierre'"

# mycursor.execute(sql)

# mydb.commit()

# sql = "UPDATE DISTRICT SET name = 'SAINT PIERRE' WHERE name = 'saint pierre'"

# mycursor.execute(sql)

# mydb.commit()

# sql = "UPDATE PLACE SET style = 'F10' WHERE STYLE = 'F1'"

# mycursor.execute(sql)

# mydb.commit()


# sql = "UPDATE CONTRACT SET client_id = 2 WHERE client_id = 1"

# mycursor.execute(sql)

# mydb.commit()


# sql = "UPDATE STYLE SET name = 'F1' WHERE name = 'f1'"

# mycursor.execute(sql)

# mydb.commit()


"""DELETE TUPLE"""



# sql = "DELETE FROM CLIENT WHERE first_name = 'pierre'"


# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

