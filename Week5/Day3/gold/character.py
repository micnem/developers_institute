class Character:
    def __init__(self, name, attack, life = 20):
        self.name = name
        self.attack = attack
        self.life = life
    def basic_attack(self,other):
        pass
class Druid(Character):
    def meditate(self):
        self.life +=10
        self.attack -= 2
        return self
    def animal_help(self):
        self.attack += 5
        return self
    def fight(self, other):
        other.life -=((0.75*self.life + 0.75*self.attack))
        return other
class Warrior(Character):
    def brawl(self, other):
        other.attack -= 2
        self.attack -=0.5
    def train(self):
        self.life += 2
        self.attack +=2
    def roar(self, other):
        other.attack -= 3
class Mage(Character):
    def curse(self, other):
        other.attack -=2
    def summon(self):
        self.attack +=3
    def cast_spell(self, other):
        other.life -= (self.attack/self.life)

d1 = Druid("Santos", 10)
m1 = Mage("Magos", 15)