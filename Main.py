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
    opponent = Wizard.Wizard()
else:
    player = Wizard.Wizard()
    opponent = Soldier.Soldier()
print("You must attack opponent")
while True:
    print("Select action")
    print("1.attack")
    print("2.block")
    print("3.counter")
    choice = input("Enter choice(1/2): ")
    response = int(random.uniform(1, 3))
    if choice == 1:
        if response == 1:
            opponent.takeDamage(player.attack())
            player.takeDamage(opponent.attack())
            print("Opponent and player take damage")
        if response == 2:
            print("Attack blocked")
        if response == 3:
            opponent.takeDamage(player.attack())
            print("opponent takes damage")
    if choice == 2:
        if response == 1:
            print("Attack blocked")
        if response == 2:
            print("Both characters blocked")
        if response == 3:
            print("Player takes damage")
            player.takeDamage(opponent.attack())

    if choice == 3:
        if response == 1:
            print("player takes damage")
            player.takeDamage(opponent.attack())
        if response == 2:
            print("Opponent takes damage")
            opponent.takeDamage(player.attack())
        if response == 3:
            print("Both players take damage")
            opponent.takeDamage(player.attack())
            player.takeDamage(opponent.attack())

    if player.isdead:
        print("Player loses the game")
        break
    elif opponent.isdead:
        print("Player loses the game")
        break
