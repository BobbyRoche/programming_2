from monster import *

class donaldT(monster):
	def __init__(self,n):
		self.__name = n
		self.__health = 30
		self.__defense_mode = False
	def __str__(self):
		return "I am a DonaldT. named "+self.__name+"."
	def getName(self):
		return self.__name
	def getDescription(self):
		return "The donaldT is useless.";
	def basicAttack(self,enemy):
		self.__defense_mode=False #Can't defend and attack
		enemy.doDamage(4)
	def basicName(self):
		return "Insults"
	def defenseAttack(self,enemy):
		self.__defense_mode=True
		#Do no damage. just defend
	def defenseName(self):
		return "THE WALL"
	def specialAttack(self,enemy):
		self.__defense_mode = False#Can't Defend and attack
		enemy.doDamage(6)
	def specialName(self):
		return "Fake News"
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