#Es fake accounts 
#import things you need 
from faker import Faker
import random 
from data import characters
fake = Faker()

#make a funtion for creating fake account
def create_fake_account():
    #make name a fake name
    name = fake.name()
    #make charater class be random from the diff classes 
    char_class = random.choice(["Warrior", "Mage", "Archer"])
    #make the levels be random number
    level = random.randint(1, 5)
    strength = random.randint(10, 5)
    speed = random.randint(10, 5)
    intelligence = random.randint(10, 5)
    #make characters be the name class level etc be themslefs
    character = {"Name": name,"Class": char_class,"Level": level,"Strength": strength,"Speed": speed,"Intelligence": intelligence}
    #append th charates to the charater list 
    characters.append(character)
    #print it 
    print(character)


