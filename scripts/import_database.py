import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Password123",
    database="trainfinder"
)

if connection.is_connected():
    print("Successfully connected to TrainFinder database!")

connection.close()