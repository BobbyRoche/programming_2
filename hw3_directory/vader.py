from enemy import Enemy
import random

class Vader(Enemy):                 #enemy subclass called vader
    def __init__(self, n, h):       #uses init of enemy and adds a dictionary of attacks and damage to be randomly selcted.
        super(Vader,self).__init__(n, h)
        self.attack_dic = {'saber throw' : 5,
                        'force choke' : 10,
                        'saber slash' : 8}
        self.attack_name = None
        self.damage = None

    def __str__(self):            #string method used to print name and helath of vader
        return str(self.name) + " " + str(self.health)

    def attack(self):            #randomly selects an attack from the dictionary to use on the player
        self.attack_name = random.choice(list(self.attack_dic.keys()))
        self.damage = self.attack_dic[self.attack_name]
        print(self.getName() + " used %s on you!" %(self.attack_name))
        return self.damage

    def takeDamage(self, other):    #used when player attacks enemy, takes away attack points from health
        self.health -= other.attack()

    def setName(self, new_name):    #changes the name of the monster
        self.name = new_name

    def setHealth(self, new_health): #changes the health of the monster if need be
        self.health = new_health


