class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


    

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

print(davids_dog.bark())
print(davids_dog.jump())
print(sarahs_dog.bark())
print(sarahs_dog.jump())
dog_list = [davids_dog, sarahs_dog]

def size_checker(dog_list):
    biggest = dog_list[0]
    for dog in dog_list:
        if dog.height > biggest.height:
            biggest = dog
    print(f"biggest dog is {biggest.name} with a height of {biggest.height}")

print(size_checker(dog_list))
