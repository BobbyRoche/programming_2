from enemy import Enemy
class Hero(Enemy):      #inherits enemy class
    def __init__(self, n, h):
        super(Hero,self).__init__(n, h)
        self.attack_dic = {'sword': 15, #dictionary of possible commands and values
                           'fireball': 30,
                           'shield': 0,
                           'potion':20}
        self.attack_name = None         #attributes used by hero
        self.attack_damage = None
        self.potion_amount = 6
        self.fireball_amount = 10


    def __str__(self):              #prints health bar and inventory of the hero
        if(self.health%1 == 0):
            self.health = int(self.health)
        return str(self.name) + "'s health: " + str(self.health) + "/100\nRemaining: " + str(self.potion_amount) + " potions and " + str(self.fireball_amount) + " fireballs."

    def attack(self):               #attacks the enemy based on the user's input. If potion is entered, no attack occurs but health is recovered
        if self.attack_name == 'sword' or self.attack_name == 'fire ball':
            print(self.getName() + " uses the %s!" % (self.attack_name))
            return self.attack_damage

        elif self.attack_name == 'potion':        #potion and fireball amounts decremented with each use. Using these when there are none left wastes you turn.
            if self.potion_amount==0:
                print("You are out of potions!")
                return 0
            else:
                print(self.getName() + " uses a %s!" % (self.attack_name))
                self.health+=self.attack_dic['potion']
                self.potion_amount -=1
                return 0
        elif self.attack_name == 'shield':  #if shield is entered nothing happens until the enemy's next attack
            print(self.getName() + " uses the %s!" % (self.attack_name))
            return 0

        elif self.attack_name == 'fireball':
            if self.fireball_amount==0:
                print("You are out of fireballs")
                return 0
            else:
                print(self.getName() + " uses %s!" % (self.attack_name))
                self.fireball_amount-=1
                return self.attack_damage

    def takeDamage(self, other):        #player takes damage from enemy. If command chosen was shield, the player will only recieve half the damage.
        if self.attack_name == 'shield':
            self.health -= other.attack() * 0.5
        else:
            self.health -= other.attack()

    def setName(self, new_name):         #used to change name and health of hero
        self.name = new_name

    def setHealth(self, new_health):
        self.health = new_health

    def setAttack(self,an):             #used to get command input from hero and set damage accordingly
        self.attack_name=an
        self.attack_damage = self.attack_dic[self.attack_name]