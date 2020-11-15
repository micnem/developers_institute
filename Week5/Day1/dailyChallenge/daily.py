class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}
    def add_animal(self, animal_name, quantity = 1):
        if animal_name not in self.animals:
            item = {animal_name:quantity}
            self.animals.update(item)
        else:
            self.animals[animal_name] = self.animals[animal_name] + 1
    def get_info(self):
        print(f"{self.name}'s farm")
        print(self.animals)
    def get_animal_types(self):
        species_list= []
        for animal in self.animals:
            species_list.append(animal)
            species_list.sort()
        return species_list


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.add_animal("sheep")
macdonald.get_info()
print(macdonald.get_animal_types())
