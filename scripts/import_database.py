from pathlib import Path

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

# Normalize train names
df["train_name"] = (
    df["train_name"]
    .astype("string")
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

# One unique train number should have one canonical name
trains = (
    df[["train_no", "train_name"]]
    .drop_duplicates()
    .drop_duplicates(subset=["train_no"], keep="first")
)

print(f"Unique trains: {len(trains)}")

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

# Prepare Train Stops
print("\nPreparing train stops...")

stop_columns = [
    "train_no",
    "stop_order",
    "station_code",
    "arrival_time",
    "departure_time",
    "distance"
]

stops = df[stop_columns].copy()

# Convert time values to datetime
stops["arrival_time"] = pd.to_datetime(stops["arrival_time"], format="%H:%M:%S", errors='coerce').dt.time
stops["departure_time"] = pd.to_datetime(stops["departure_time"], format="%H:%M:%S", errors='coerce').dt.time

#insert Train Stops
print("\nInserting Train Stops......")
stop_query="""
insert into train_stops (train_no, stop_order,station_code, arrival_time, departure_time, distance)
values (%s, %s, %s, %s, %s, %s)
"""
stop_data=list(
    stops.itertuples(index=False, name=None)
)
#cursor.executemany(stop_query, stop_data)

print(f"Inserted train stops: {cursor.rowcount}")

#commit the changes
connection.commit()

print("\n==========================")
print("Data import completed successfully!")
print("==========================")

#Close the cursor and connection
cursor.close()
connection.close()

print("\n MySQL Database connection closed.")