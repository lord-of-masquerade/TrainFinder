from pathlib import Path
import pandas as pd

#project path 
ROOT = Path(__file__).resolve().parent.parent
RAW_FILE = ROOT / "data" / "raw" / "railway_data.csv" #change the file name to your raw data file name
OUTPUT_FILE = ROOT / "data" / "processed" / "railway_data_clean.csv"

# Create processed directory if it doesn't exist
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

#loading the dataset
#read csv file
print("reading dataset...")
df=pd.read_csv(RAW_FILE)
print("\n====== Original Dataset ======")
print(f"Rows : {len(df)}")
print(f"Columns: {len(df.columns)}")

#renaming the columns
df.rename(columns={
    "Train No.": "train_no",
    "train Name": "train_name",
    "islno": "stop_order",
    "station Code": "station_code",
    "Station Name": "station_name",
    "Arrival time": "arrival_time",
    "Departure time": "departure_time",
    "Distance": "distance",
    "Source Station Code": "source_station_code",
    "source Station Name": "source_station_name",
    "Destination station Code": "destination_station_code",
    "Destination Station Name": "destination_station_name"
}, inplace=True)

#clean text columns
text_columns = [
    "train_no",
    "train_name",
    "station_code",
    "station_name",
    "source_station_code",
    "source_station_name",
    "destination_station_code",
    "destination_station_name"
]
for col in text_columns:
    df[col]=(df[col].astype(str).str.strip().str.replace("'","",regex=False))

# Convert Data Types
df["stop_order"] = pd.to_numeric(df["stop_order"], errors="coerce")
df["distance"] = pd.to_numeric(df["distance"], errors="coerce")

#missing values
print("\n====== Missing Values ======")
print(df.isnull().sum())

#duplicates rows
duplicates = df.duplicated().sum()

print(f"\nDuplicates Rows Found: {duplicates}")

if duplicates > 0:
    df=df.drop_duplicates()

#Save the cleaned dataset
df.to_csv(OUTPUT_FILE, index=False)

print("\n====== Final Summary ======")
print(f"rows: {len(df)}")
print(f"Unique Trains: {df['train_no'].nunique()}")
print(f"Unique Stations: {df['station_code'].nunique()}")


print(f"\nCleaned dataset saved to: {OUTPUT_FILE}")