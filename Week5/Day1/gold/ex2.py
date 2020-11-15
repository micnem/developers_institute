import random
class MyList:
    def __init__(self,some_list):
        self.some_list = some_list
    def reverser(self):
        self.some_list.reverse()
        print(self.some_list)
       
    def sorter(self):
        self.some_list.sort()
        print(self.some_list)
    def randomizer(self):
        new_list = [random.randint(0,len(self.some_list)) for item in self.some_list]
        print(new_list)
    
animal_list = MyList(['Ape', 'Baboon', 'Bear', 'Cat', 'Cougar', 'Eel', 'Emu'])
animal_list.reverser()
animal_list.sorter()
animal_list.randomizer()