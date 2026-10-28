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

# Load Clean Dataset

print("\nReading cleaned dataset...")
df = pd.read_csv(CLEAN_FILE)
print(f"Rows loaded: {len(df)}")

#prepare the train data for insertion into the database
trains=df[
    ["train_no","train_name"]
].drop_duplicates()

print(f"Unique trains: {len(trains)}")