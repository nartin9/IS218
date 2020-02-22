import Soldier
import Wizard
import random

player = None
opponent = None
print("Select Class")
print("1.Soldier")
print("2.Wizard")
choice = input("Enter choice(1/2): ")
if choice == "1":
    player = Soldier.Soldier()
    player.createStats()
    opponent = Wizard.Wizard()
    opponent.createStats()
else:
    player = Wizard.Wizard()
    player.createStats()
    opponent = Soldier.Soldier()
    opponent.createStats()
player.stats()
print("You must attack opponent")
while True:
    print("Select action")
    print("1.attack")
    print("2.block")
    print("3.counter")
    choice = int(input("Enter choice(1/2): "))
    response = int(random.randint(1, 3))
    if choice == 1:
        if response == 1:
            opponent.takeDamage(int(player.attack()))
            player.takeDamage(int(opponent.attack()))
            print("Opponent and player take damage")
        if response == 2:
            print("Attack blocked")
        if response == 3:
            opponent.takeDamage(int(player.attack()))
            print("opponent takes damage")
    if choice == 2:
        if response == 1:
            print("Attack blocked")
        if response == 2:
            print("Both characters blocked")
        if response == 3:
            print("Player takes damage")
            player.takeDamage(int(opponent.attack()))

    if choice == 3:
        if response == 1:
            print("player takes damage")
            player.takeDamage(int(opponent.attack()))
        if response == 2:
            print("Opponent takes damage")
            opponent.takeDamage(int(player.attack()))
        if response == 3:
            print("Both players take damage")
            opponent.takeDamage(int(player.attack()))
            player.takeDamage(int(opponent.attack()))

    if player.isdead():
        print(response)
        print("Player loses the game")
        break
    elif opponent.isdead():
        print("Player wins the game")
        break
