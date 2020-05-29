from enemy import Enemy


class Ugandan_knuckles(Enemy):          #sublcass of enemy called Ugandan Knuckles
    def __init__(self, n, h):           #uses enemy init for name and health, creates two of its own attributes
        super(Ugandan_knuckles,self).__init__(n, h,)
        self.attack_name = 'spit acid'
        self.damage = 6

    def __str__(self):                  #string method used if one wishes to see the name and health of the enemy
        return str(self.name) + " " + str(self.health)

    def attack(self):            #method used to attack the player
        print(self.getName() + " %s on you!" %(self.attack_name))
        return self.damage

    def takeDamage(self, other):    #used when player attacks enemy, takes away attack points from health
        self.health -= other.attack()

    def setName(self, new_name):    #changes the name of the monster
        self.name = new_name

    def setHealth(self, new_health): #changes the health of the monster if need be
        self.health = new_health
