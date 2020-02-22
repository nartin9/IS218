import random
import Character


class Soldier(Character.Character):

    def Soldier(self):
        attack = int(random.uniform(1, 10)) + 2
        defense = int(random.uniform(1, 10)) + 2
        speed = int(random.uniform(1, 10))
        intelligence = int(random.uniform(1, 10))
        hp = int(random.uniform(1, 10))

    def attack(self):
        return self.attack

    def block(self):
        return self.defense


