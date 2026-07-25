from pathlib import Path
import pandas as pd

#project path 
ROOT = Path(__file__).parent.parent
RAW_FILE = ROOT / "data" / "raw" / "railway_data.csv"
OUTPUT_FILE = ROOT / "data" / "processed" / "railway_data_clean.csv"

#read csv file
print("reading dataset...")
df=pd.read_csv(RAW_FILE)
print("\n====== Dataset Info ======")
print(f"rows: {df.shape[0]}")
print(f"columns: {df.shape[1]}")
print("\ncolumns: ")
print(df.columns.tolist())
