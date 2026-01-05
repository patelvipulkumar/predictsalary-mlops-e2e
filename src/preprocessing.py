import pandas as pd

def main():
    df = pd.read_csv("data/raw/empexpsaldataset.csv")

    # Basic text normalization (can be extended later)
   
    # Save processed data
    df.to_csv("data/processed/empexpsalclean.csv", index=False)

    print("✅ Preprocessing completed")

if __name__ == "__main__":
    main()