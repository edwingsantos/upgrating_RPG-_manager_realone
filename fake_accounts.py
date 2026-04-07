from faker import Faker
import random 
from load import characters
fake = Faker()

def create_fake_account():
    name = fake.name()

    char_class = random.choice(["Warrior", "Mage", "Archer"])

    level = random.randint(1, 50)
    strength = random.randint(10, 100)
    speed = random.randint(10, 100)
    intelligence = random.randint(10, 100)

    character = {
        "Name": name,
        "Class": char_class,
        "Level": level,
        "Strength": strength,
        "Speed": speed,
        "Intelligence": intelligence
    }

    characters.append(character)

    print("Fake character created!")
    print(character)


