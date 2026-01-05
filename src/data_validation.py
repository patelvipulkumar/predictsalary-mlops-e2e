import pandas as pd

def main():
    df = pd.read_csv("data/raw/empexpsaldataset.csv")

     # 2. Basic Validation Checks
    print("\n--- Running Validations ---")
    # Check for duplicates
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"Validation: Found {duplicates} duplicate rows. Removing them...")
        df = df.drop_duplicates()
    
    # Check for missing values
    missing = df.isnull().sum()
    print(f"Missing values per column:\n{missing}")

if __name__ == "__main__":
    main()