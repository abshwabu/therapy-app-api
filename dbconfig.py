import mysql.connector

db = mysql.connector.connect(

    host= 'localhost',
    user = 'root',
    passwd = 'password123',

)

cursor = db.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS therapy_app_db')

print('Created database')