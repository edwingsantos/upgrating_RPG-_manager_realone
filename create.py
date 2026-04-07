#ES create file 
from data import characters
from faker import Faker
fake = Faker()



def create():
    name = input("Enter name: ")

    print("Choose class:")
    print("1 Warrior\n2 Mage\n3 Archer")
    c = input("Choice ")

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
