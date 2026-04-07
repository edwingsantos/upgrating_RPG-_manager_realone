from faker import Faker
import random

fake = Faker()

class RandomGenerator:
    def generate_character(self):
        return (
            fake.name(),
            random.choice(["Warrior", "Mage", "Archer"]),
            random.randint(1, 20),
            {
                "Strength": random.randint(1, 100),
                "Speed": random.randint(1, 100),
                "Intelligence": random.randint(1, 100)
            }
        )

    def backstory(self):
        return fake.text(max_nb_chars=150)