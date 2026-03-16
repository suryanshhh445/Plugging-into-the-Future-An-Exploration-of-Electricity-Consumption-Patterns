import pandas as pd
import os

# --- Configuration ---
CSV_FILE_PATH = r'c:\Users\yuggu\Workstation\Tableau Project\Consumption (1).csv.xls'
CLEANED_CSV_PATH = r'c:\Users\yuggu\Workstation\Tableau Project\cleaned_consumption_data.csv'

def clean_column_names(df):
    """Standardizes column names to be database-friendly."""
    cols = df.columns
    new_cols = [col.strip().lower().replace(' ', '_').replace('(', '').replace(')', '') for col in cols]
    df.columns = new_cols
    return df

def prepare_data_for_tableau():
    """
    Reads electricity consumption data from a CSV, cleans it,
    and saves it as a new, clean CSV file for Tableau Public.
    """
    if not os.path.exists(CSV_FILE_PATH):
        print(f"Error: The file '{CSV_FILE_PATH}' was not found.")
        return

    print("--- Starting Data Loading Process ---")

    # 1. Read and Clean Data with Pandas
    print(f"Reading data from '{CSV_FILE_PATH}'...")
    df = pd.read_csv(CSV_FILE_PATH)
    df = clean_column_names(df)

    # Convert 'dates' column to datetime objects, handling the 'DD/MM/YYYY' format
    print("Converting date column to the correct format...")
    df['dates'] = pd.to_datetime(df['dates'], dayfirst=True)

    print("Data after cleaning and type conversion:")
    print(df.head())
    print("\nData Info:")
    df.info()

    # 2. Save the cleaned data to a new CSV file
    try:
        print(f"\nSaving cleaned data to '{CLEANED_CSV_PATH}'...")
        df.to_csv(CLEANED_CSV_PATH, index=False)
        print(f"Successfully created '{CLEANED_CSV_PATH}'. You can now use this file in Tableau Public.")
    except Exception as e:
        print(f"Error saving file: {e}")

    print("--- Data Loading Process Finished ---")

if __name__ == '__main__':
    prepare_data_for_tableau()
