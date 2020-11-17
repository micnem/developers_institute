class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return("barks.")
    def run_speed(self):
        speed = self.weight / (self.age * 10)
        return speed
    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            print(f"{self.name} is the winner")
        else:
            print(f"{other_dog.name} is the winner")

# d1 = Dog("Toby", 3, 20)
# d2 = Dog("Rex", 2, 30)
# d3 = Dog("Spot", 1, 12)
# d1.fight(d3)