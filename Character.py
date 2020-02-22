class Character:
    attack = 0
    defense = 0
    speed = 0
    intelligence = 0
    hp = 0

    def attack(self):
        return self.attack

    def block(self):
        return self.defense

    def takeDamage(self, damage):
        self.hp = self.hp - damage

    def stats(self):
        print("Attack =" + self.attack)
        print("Defence =" + self.defence)
        print("Speed =" + self.speed)
        print("Intelligence =" + self.intelligence)
        print("HP =" + self.hp)

    def isdead(self):
        return self.hp >= 0
