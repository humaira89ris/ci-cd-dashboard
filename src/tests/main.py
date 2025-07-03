import pandas as pd
import os

def load_and_process_data(filepath="data/dataset.csv", output_path="data/processed_dataset.csv"):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Input file not found: {filepath}")

    df = pd.read_csv(filepath)
    df = df.drop_duplicates()
    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    load_and_process_data()
