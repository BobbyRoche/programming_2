#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172
from random import randint
from Dino import *
from Cracken import *
from dragon import *
from donaldT import *
import random
import time


def main():
	first = dragon("Dink")
	second = donaldT("pres")
	third = Dino("Drogo")
	fourth = Cracken("Jack")

	monsterlist = []
	monsterlist.append(first)
	monsterlist.append(second)
	monsterlist.append(third)
	monsterlist.append(fourth)
	i = randint(0,3)
	fighter1 = monsterlist[i]
	monsterlist.remove(monsterlist[i])
	i = randint(0, 2)
	fighter2 = monsterlist[i]
	monsterlist.remove(monsterlist[i])
	i = randint(0, 1)
	fighter3 = monsterlist[i]
	monsterlist.remove(monsterlist[i])
	fighter4 = monsterlist[0]



	ans = input("Are you ready to begin the tournament?(press y when ready)")

	winner = monster_battle(fighter1,fighter2)

	ans = input("Are you ready for the next battle?(press y when ready)")
	if(ans == "y"):
		winner2 = monster_battle(fighter3,fighter4)

	ans = input("Are you ready for the final battle?(press y when ready)")
	if (ans == "y"):
		champion = monster_battle(winner, winner2)
	print(champion.getName() + " is the champion!")



#DO NOT make any changes below this line
#---------------------------------------------------

#This function has two monsters fight
#it returns the winner
#or None on a tie
def monster_battle(m1, m2):
	#Type Check
	if not issubclass(type(m1),monster):
		print("First Monster is not a subclass of monster class.")
		return None
	if not issubclass(type(m2),monster):
		print("Second Monster is not a subclass of monster class")
		return None

	m1.resetHealth()
	m2.resetHealth()

	print("Starting Battle Between")
	print(m1.getName()+": "+m1.getDescription())
	print(m2.getName()+": "+m2.getDescription())
	
	#Record start time
	#if 30 seconds pass then timeout
	#This is the current time in seconds since Unix Epoch
	start_time = time.time()
	timeout = False

	#Whose turn is it?
	attacker = None
	defender = None
	#Select Randomly
	if(random.randint(0,1) == 0):
		#m1 goes first
		attacker = m1
		defender = m2
	else:
		#m2 goes first
		attacker = m2
		defender = m1
	print(attacker.getName()+" goes first.")
	#Loop until either 1 is unconscious or timeout
	while( m1.getHealth() > 0 and m2.getHealth() > 0 and not timeout):
		#Determine what move the monster makes
		#Probabilities:
		#	60% chance of standard attack
		#	20% chance of defense move
		#	20% chance of special attack move

		#Pick a number between 1 and 100
		move = random.randint(1,100)
		#It will be nice for output to record the damage done
		before_health=defender.getHealth()
		if( move >=1 and move <= 60):
			#Attack!
			attacker.basicAttack(defender)
			print_results(attacker,defender,attacker.basicName(),before_health-defender.getHealth())
		elif move>=61 and move <= 80:
			#Defend!
			attacker.defenseAttack(defender)
			print_results(attacker,defender,attacker.defenseName(),before_health-defender.getHealth())
		else:
			#Special Attack!
			attacker.specialAttack(defender)
			print_results(attacker,defender,attacker.specialName(),before_health-defender.getHealth())
		#Swap attacker and defender
		tmp = attacker
		attacker = defender
		defender = tmp

		#Check for a timeout
		if(time.time() - start_time > 30):
			timeout = True
		print(m1.getName()+" at "+str(m1.getHealth()))
		print(m2.getName()+" at "+str(m2.getHealth()))
	#Determine Results of the match
	if(m1.getHealth() < 1 and m2.getHealth() < 1):
		print("Both Monsters are unconscious the match is a tie")
		return None
	if(m1.getHealth() < 1):
		print(m2.getName()+" is victorious!")
		return m2
	if(m2.getHealth() < 1):
		print(m1.getName()+" is victorious!")
		return m1
	if timeout:
		print("Battle is ended by timeout. It is a tie.")
		return None
	print("A tie. It is not clear why. This is probably a bug.")
	return None
#Print status updates
def print_results(attacker,defender,attack,hchange):
	res=attacker.getName()+" used "+attack
	res+=" on "+defender.getName()+"\n"
	res+="The attack did "+str(hchange)+" damage."
	print(res)

#----------------------------------------------------
if __name__=="__main__":
	#Every battle should be different, so we need to
	#start the random number generator somewhere "random".
	#With no input Python will set the seed
	random.seed()
	main()