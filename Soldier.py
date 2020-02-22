import random
import Character


class Soldier(Character.Character):
    pass

    def createStats(self):
        self.damage = random.randint(1, 10) + 2
        self.defense = random.randint(1, 10) + 2
        self.speed = random.randint(1, 10)
        self.intelligence = random.randint(1, 10)
        self.hp = random.randint(1, 10)

    def block(self):
        return self.defense


