#ES create file 
#import all things required
from data import characters
from faker import Faker
fake = Faker()

#make a funtion for create 
def create():
    #make name an input asking for the name 
    name = input("Enter name: ")
    #print to choose the class and make them input it 
    print("Choose class:")
    print("1 Warrior\n2 Mage\n3 Archer")
    choice = input("Choice ")
    #if choice is 1 make the class warrior
    if choice == "1":
        char_class = "Warrior"
    #elif choice is 2 make the class mage
    elif choice == "2":
        char_class = "Mage"
    #elif choice is 3 make the class archer
    elif choice == "3":
        char_class = "Archer"
    #else print invalid class and retunr
    else:
        print("Invalid class")
        return
    #make the user input the levels 
    try:
        level = int(input("Level: "))
        strength = int(input("Strength: "))
        speed = int(input("Speed: "))
        intelligence = int(input("Intelligence: "))
    #else print there is an invalid number and return 
    except:
        print("Invalid number")
        return
    #append the names, class, level, strecht, speed, inteligence as themselfs
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
