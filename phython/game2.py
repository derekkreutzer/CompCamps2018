import random
import sys

class human:
     """the guard."""
     def __init__(self, name):
         self.name= name
         self.heath=15
         self.damage =random.randint(1,5)
     def damage(self):
         return random.randint(1,7)

     def isAlive(self):
         return self.heath > 0

     def attack(self):
         damage = random.randint(0,10)
         self.heath-= damage
         return damage


print ("gaurd:oh my is that the master of the voil  ")
theMaster = input("well is it y-n")
if "y" == theMaster:
    print("gaurd:now that i think about it you are not him sum")
    print("the gaurd draws his sword amd slits your neck och!")
    sys.exit(0)
else:
    print("oh sorry my old eye don`t see as well as they should")
    name = input (" what is your name sir? ")

    print("gaurd: welcome to the void travaler {}".format(name))
    print("gaurd: in ouder to enter it is fifty gold coins!")
    print
    payingTheFine = input("gaurd: will you pay? y-n ")

if "y"== payingTheFine:
    print("gaurd: very good you are very smart")
    print("gaurd: you my be on your way")
    print("you go on to have a boring life you dumb dumb")
else:
    print("gaurd: fine have it your way ")
    print("the gaurd is draing his short sword ")
    print("do you fight or flee ")



health = 20

score=0

guard=human ("the guard")

while guard.isAlive():
    print("You have {} health.".format(health))
    print("Do you want to fight or flee?")
    if input("Fight / Flee > ").lower() == "fight":
        damage = guard.attack()
        score += damage
        print("You did {} damage!".format(damage))
        if guard.isAlive():
            damage = guard.damage
            health -= damage
            print("You took {} damage!".format(damage))
    else:
        caught = random.randint(1,5) == 1
        if not caught:
            print("You have escaped!")
            print("Your score was {}".format(score))
            sys.exit(0)
        else:
            print("You failed to run away!")
