import ex2
import random
class PetDog(ex2.Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained  = trained
    def train(self):
        self.trained = True
    def play(self, *args):
        playing_dogs = []
        for dog in list(args) + [self]:
            if self.trained == True:
                self.trained = False
            playing_dogs.append(dog.name)
        playing_dogs = " and ".join(playing_dogs)
        print(f"{self.name} is playing with {playing_dogs}")

    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on their back legs", "shakes your hand", "plays dead"]
        if self.trained == True:
            print(f"{self.name} {random.choice(tricks)}")
    

d4 = PetDog("Tommy", 3, 34)
d5 = PetDog("Long", 2, 24)
d6 = PetDog("Samm" ,6, 14)
d7 = PetDog("Oscar",1, 23)
d7.train()
d7.do_a_trick()
d4.play(d5,d6, d7)
