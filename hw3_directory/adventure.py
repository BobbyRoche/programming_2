from hero import Hero
from dragon import Dragon
from zombie import Zombie
from ugandan_knuckles import Ugandan_knuckles
from vader import Vader
import random
import sys



def battle():   #this method runs through the battles. Depending on how many were chosen, once all battles are complete it will return the winner
    i=0
    while i < len(enemy_list):
        enemy = enemy_list[i]   #keeps track of the randomly selected list of enemies.
        print("You will fight: %s"%(enemy.getName()))       #battle which allows user to enter commands to fight the enemy
        while hero.getHealth()>0:
            print(hero)
            action = input("\nEnter Command: sword shield fireball potion exit:\n")
            try:                    # if the input is not a command or exit, it will reloop without moving on to another enemy or move
                hero.setAttack(action)
            except KeyError:
                if action == 'exit':    #if exit is entered the game is over
                    print("Thanks for playing!")
                    sys.exit()
                print("Your command is invalid.")
                i=0
                continue
            enemy.takeDamage(hero)      #handling of command, and enemy attack portion
            if enemy.getHealth()<=0:
                print("\nYou have defeated %s\n\n" % (enemy.getName()))
                break
            hero.takeDamage(enemy)
            if hero.getHealth()<=0:
                return False
        i+=1
    return True

def getNumber():
    try:
        return int(input("How many enemies do you want to battle?\n"))

    except ValueError:
        print("Must be an int")
        return getNumber()
#random.seed(0)
    
print("Welcome to the adventure!\n")        #opener, and prompts user hero's name
hero_name = input("What is the hero's name?\n")
hero = Hero(hero_name,100)

num_enemies = getNumber()   #calls method to get number of enemies which also handles improper input

enemy_list=[]
i=0
while i<num_enemies:        #randomly selects proper number of enemies
    num = random.randint(0,3)
    if num == 0:
        enemy_list.append(Dragon("Drogon",100))
    elif num == 1:
        enemy_list.append(Zombie("Walker",70))
    elif num == 2:
        enemy_list.append(Ugandan_knuckles("Brudah",60))
    elif num == 3:
        enemy_list.append(Vader("Darth Vader",100))
    i+=1
winner = battle()   #gets the winner
if winner == False: #results of the game
    print("You are dead.")
    sys.exit()
else:
    print("Congratulations you have emerged victorious!")
    sys.exit()
