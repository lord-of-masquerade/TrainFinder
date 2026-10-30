from pathlib import path

import pandas as pd
import mysql.connector

ROOT = Path(__file__).resolve().parent.parent
CLEAN_FILE=ROOT / "data" / "processed" / "railway_data_clean.csv"


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@PassCode002.",
    database="trainfinder"
)

cursor = connection.cursor()
print("Successfully connected to TrainFinder database!")

# Load Clean Dataset

print("\nReading cleaned dataset...")
df = pd.read_csv(CLEAN_FILE)
print(f"Rows loaded: {len(df)}")

#prepare the train data for insertion into the database
trains=df[
    ["train_no","train_name"]
].drop_duplicates()

print(f"Unique trains: {len(trains)}")

# Prepare Station Data
stations=df[
    ["station_code","station_name"]
].drop_duplicates() 

print(f"Unique stations: {len(stations)}")

#Insert Trains

print("\nInserting Trains......")

train_query="""
insert into trains (train_no, train_name)
values (%s, %s)
"""
train_data=list(
    trains.itertuples(index=False, name=None)
)
cursor.executemany(train_query, train_data)
print(f"Inserted stations: {cursor.rowcount}")

#Insert Stations

print("\nInserting Stations......")

station_query="""
insert into stations (station_code, station_name)
values (%s, %s)
"""

station_data=list(
    stations.itertuples(index=False, name=None)
)
cursor.executemany(station_query, station_data)
print(f"Inserted stations: {cursor.rowcount}")  
