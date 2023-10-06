import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

#Cursor object

cursor_object = dataBase.cursor()

#Create a database

cursor_object.execute("CREATE DATABASE elderco")
print("Good to GO!")
