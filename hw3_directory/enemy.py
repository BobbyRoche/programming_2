#Robert Roche
#CS-172 Section A, Lab 062
import abc

class Enemy:                #enemy base class
   def __init__(self,n,h):  #initializes only name and health, something all monsters will have
        self.name = n
        self.health = h
   def getName(self):       #a method to return the name, and one to return the health
       return self.name
   def getHealth(self):
       return self.health
   @abc.abstractmethod      # the abstract methods to be overriden by each subclass.
   def  takeDamage(self,other):
       pass
   @abc.abstractmethod
   def attack(self,other):
       pass
