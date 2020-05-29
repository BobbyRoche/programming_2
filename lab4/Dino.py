#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172

#This is a hamster.
#It is a very weak monster.
from monster import *

class Dino(monster):
	def __init__(self,n):
		self.__name = n
		self.__health = 30
		self.__defense_mode = False
	def __str__(self):
		return "I am a Dino named "+self.__name+"."
	def getName(self):
		return self.__name
	def getDescription(self):
		return "The Dino is both fluffy and friendly.";
	def basicAttack(self,enemy):
		self.__defense_mode=False #Can't defend and attack
		enemy.doDamage(5)
	def basicName(self):
		return "Duck"
	def defenseAttack(self,enemy):
		self.__defense_mode=True
		#Do no damage. just defend
	def defenseName(self):
		return "Kick"
	def specialAttack(self,enemy):
		self.__defense_mode = False#Can't Defend and attack
		enemy.doDamage(3)
	def specialName(self):
		return "Tallest Guy"
	def getHealth(self):
		return self.__health
	def doDamage(self,damage):
		if(self.__defense_mode):
			#Half Damage
			self.__health=self.__health-(damage//2)
		else:
			self.__health=self.__health-damage
	def resetHealth(self):
		self.__health=30