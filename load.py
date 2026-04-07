#ES load file
import os 
import pandas as pd
from data import CSV_FILE, characters


def load_data():
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        for _, row in df.iterrows():
            characters.append({
                "Name": row["Name"],
                "Class": row["Class"],
                "Level": row["Level"],
                "Strength": row["Strength"],
                "Speed": row["Speed"],
                "Intelligence": row["Intelligence"]
            })
        print("Loaded user.csv")

def save():
    if not characters:
        print("No data to save")
        return

    df = pd.DataFrame(characters)
    df.to_csv(CSV_FILE, index=False)
    print("Saved to user.csv")

def stats():
    if not characters:
        print("No characters")
        return

    df = pd.DataFrame(characters)
    print(df)
    print("\nStats:\n", df.describe())