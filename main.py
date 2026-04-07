import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker
import os
import math

fake = Faker()
CSV_FILE = "user.csv"

characters = []

# -------------------------
# LOAD DATA
# -------------------------
def load():
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

# -------------------------
# SAVE DATA
# -------------------------
def save():
    if not characters:
        print("No data to save")
        return

    df = pd.DataFrame(characters)
    df.to_csv(CSV_FILE, index=False)
    print("Saved to user.csv")

# -------------------------
# CREATE CHARACTER (USER INPUT)
# -------------------------
def create():
    name = input("Enter name: ")

    print("Choose class:")
    print("1 Warrior\n2 Mage\n3 Archer")
    c = input("> ")

    if c == "1":
        char_class = "Warrior"
    elif c == "2":
        char_class = "Mage"
    elif c == "3":
        char_class = "Archer"
    else:
        print("Invalid class")
        return

    try:
        level = int(input("Level: "))
        strength = int(input("Strength: "))
        speed = int(input("Speed: "))
        intelligence = int(input("Intelligence: "))
    except:
        print("Invalid number")
        return

    characters.append({
        "Name": name,
        "Class": char_class,
        "Level": level,
        "Strength": strength,
        "Speed": speed,
        "Intelligence": intelligence
    })

    print("Character created!")
    print("Backstory:", fake.text(max_nb_chars=120))

# -------------------------
# SHOW STATS
# -------------------------
def stats():
    if not characters:
        print("No characters")
        return

    df = pd.DataFrame(characters)
    print(df)
    print("\nStats:\n", df.describe())

# -------------------------
# GRAPH
# -------------------------
def graph():
    if not characters:
        print("No characters")
        return

    for i, c in enumerate(characters):
        print(i, c["Name"])

    try:
        i = int(input("Pick: "))
        c = characters[i]
    except:
        print("Invalid")
        return

    labels = ["Strength", "Speed", "Intelligence"]
    values = [c[l] for l in labels]

    angles = [n / float(len(labels)) * 2 * math.pi for n in range(len(labels))]
    values += values[:1]
    angles += angles[:1]

    plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    plt.title(c["Name"])
    plt.show()

# -------------------------
# MENU
# -------------------------
def main():
    load()

    while True:
        print("""
        1 Create Character
        2 Show Stats
        3 Graph Character
        4 Save
        5 Exit
        """)

        choice = input("> ")

        if choice == "1":
            create()
        elif choice == "2":
            stats()
        elif choice == "3":
            graph()
        elif choice == "4":
            save()
        elif choice == "5":
            save()
            break
        else:
            print("Invalid")

main()