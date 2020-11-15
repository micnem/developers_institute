class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print("animal already in this zoo")
    def get_animals(self):
        print(self.animals)
    def sell_animal(self,animal_sold):
        self.animals.remove(animal_sold)
    def sort_animals(self):
        self.animals.sort()
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        new_list = []
        animal_dictionary = {}
        for letter in alphabet:
            sublist = []
            for animal in self.animals:
                if animal[0].lower() == letter.lower():
                    sublist.append(animal)
            if sublist:
                new_list.append(sublist)
        
        for index,animal in enumerate(new_list):
            animal_dictionary.update({index + 1: animal})
        print(animal_dictionary)




zoo1 = Zoo("London Zoo")
zoo1.animals = ["Baboon", "Bear","Cat", "Cougar", "Eel", "Emu"]
zoo1.add_animal("Ape")
zoo1.sort_animals()

