import random
import Character


class Wizard(Character.Character):

    def Wizard(self):
        attack = int(random.uniform(1, 10))
        defense = int(random.uniform(1, 10))
        speed = int(random.uniform(1, 10))
        intelligence = int(random.uniform(1, 10)) + 5
        hp = int(random.uniform(1, 10))

    def attack(self):
        return self.intelligence


