#ES load file
#import the things needed 
import os 
import pandas as pd
from data import CSV_FILE, characters

#make a funtion to load data 
def load_data():
    #if the os path exsits of the csv file make df read the file 
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        #make a loop in the rows and add the names class ect 
        for i, row in df.iterrows():
            characters.append({"Name": row["Name"], "Class": row["Class"], "Level": row["Level"], "Strength": row["Strength"], "Speed": row["Speed"], "Intelligence": row["Intelligence"]})
#make a funtion for save 
def save():
    #if there is nothing in characters print that there is no data to safe
    if not characters:
        print("No data to save")
        return
    #make a table from character, and safe the file 
    df = pd.DataFrame(characters)
    df.to_csv(CSV_FILE, index=False)
#make a funtion 
def stats():
    #if there is no characters say that there is no character
    if not characters:
        print("No characters")
        return
    #make a table for the characters and print them 
    df = pd.DataFrame(characters)
    print(df)
    print("\nStats:\n", df.describe())