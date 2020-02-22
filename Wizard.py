import random
import Character


class Wizard(Character.Character):
    pass

    def createStats(self):
        self.damage = random.randint(1, 10)
        self.defense = random.randint(1, 10)
        self.speed = random.randint(1, 10)
        self.intelligence = random.randint(1, 10) + 5
        self.hp = random.randint(1, 10)

    def attack(self):
        return self.intelligence


