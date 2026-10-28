from pathlib import path
import mysql.connector

ROOT=Path(__file__).resolve().parent.parent
CLEAN_FILE=ROOT / "data" / "processed" / "railway_data_clean.csv"


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@PassCode002.",
    database="trainfinder"
)

cursor = connection.cursor()
print("Successfully connected to TrainFinder database!")

connection.close()