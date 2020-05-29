from monster import *

class ugandan_knuckles(monster):
	def __init__(self,n):
		self.__name = n
		self.__health = 20
		self.__defense_mode = False
	def __str__(self):
		return "I am named "+self.__name+"."
	def getName(self):
		return self.__name
	def getDescription(self):
		return "The ugandan knuckles wants to know de wae.";
	def basicAttack(self,enemy):
		self.__defense_mode=False #Can't defend and attack
		enemy.doDamage(4)
	def basicName(self):
		return "Punch"
	def defenseAttack(self,enemy):
		self.__defense_mode=True
		#Do no damage. just defend
	def defenseName(self):
		return "Duck and cover"
	def specialAttack(self,enemy):
		self.__defense_mode = False#Can't Defend and attack
		enemy.doDamage(7)
	def specialName(self):
		return "Spit"
	def getHealth(self):
		return self.__health
	def doDamage(self,damage):
		if(self.__defense_mode):
			#Half Damage
			self.__health=self.__health-(damage//2)
		else:
			self.__health=self.__health-damage
	def resetHealth(self):
		self.__health=20