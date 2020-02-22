class Character:
    damage = 2
    defense = 0
    speed = 0
    intelligence = 0
    hp = 0

    def createStats(self):
        self.damage = random.random_integers(1, 10)
        self.defense = random.random_integers(1, 10)
        self.speed = random.random_integers(1, 10)
        self.intelligence = random.random_integers(1, 10)
        self.hp = random.random_integers(1, 10)

    def attack(self):
        return self.damage

    def block(self):
        return self.defense

    def takeDamage(self, damage):
        self.hp = self.hp - damage

    def stats(self):
        print("Attack =", self.damage)
        print("Defence =", self.defense)
        print("Speed =", self.speed)
        print("Intelligence =", self.intelligence)
        print("HP =", self.hp)

    def isdead(self):
        return self.hp <= 0
