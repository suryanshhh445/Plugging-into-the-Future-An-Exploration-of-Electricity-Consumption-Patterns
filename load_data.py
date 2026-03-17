import pandas as pd
from pathlib import Path

# --- Configuration ---
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
RAW_CSV_NAME = 'Consumption (1).csv.xls'
CLEANED_CSV_NAME = 'cleaned_consumption_data.csv'
CSV_FILE_PATH = DATA_DIR / RAW_CSV_NAME
CLEANED_CSV_PATH = OUTPUT_DIR / CLEANED_CSV_NAME

def clean_column_names(df):
    """
    Standardizes dataframe column names by converting to lowercase, 
    stripping whitespace, and replacing spaces with underscores.
    """
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace(r"[()]", "", regex=True)
    )
    return df

def prepare_data_for_tableau():
    """
    Main data pipeline execution:
    Reads raw CSV, applies cleaning transformations, and exports for visualization.
    """
    if not CSV_FILE_PATH.exists():
        print(f"[ERROR] The file '{CSV_FILE_PATH}' was not found.")
        print(f"[INFO] Please make sure you have a '{DATA_DIR}' folder with '{RAW_CSV_NAME}' inside it.")
        return

    print("--- Starting Data Preparation ---")

    # 1. Read and Clean Data with Pandas
    print(f"[INFO] Reading data from '{CSV_FILE_PATH}'...")
    df = pd.read_csv(CSV_FILE_PATH)
    df = clean_column_names(df)

    # Convert 'dates' column to datetime objects, handling the 'DD/MM/YYYY' format
    print("[INFO] Converting 'dates' column to datetime format...")
    df['dates'] = pd.to_datetime(df['dates'], dayfirst=True)

    print("[INFO] Data after cleaning and type conversion (first 5 rows):")
    print(df.head())
    print("\n[INFO] DataFrame Info:")
    df.info()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 2. Save the cleaned data to a new CSV file
    try:
        print(f"\n[INFO] Saving cleaned data to '{CLEANED_CSV_PATH}'...")
        df.to_csv(CLEANED_CSV_PATH, index=False)
        print(f"[SUCCESS] Created '{CLEANED_CSV_PATH}'. You can now use this file in Tableau Public.")
    except Exception as e:
        print(f"[ERROR] Could not save the file: {e}")

    print("--- Data Preparation Finished ---")

if __name__ == '__main__':
    prepare_data_for_tableau()
