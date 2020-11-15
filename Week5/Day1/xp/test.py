animals = ['Ape', 'Baboon', 'Bear', 'Cat', 'Cougar', 'Eel', 'Emu']
alphabet = "abcdefghijklmnopqrstuvwxyz"
new_list = []
for letter in alphabet:
    sublist = []
    for animal in animals:
        if animal[0].lower() == letter.lower():
            sublist.append(animal)
    if sublist:
        new_list.append(sublist)


animal_dictionary = {}
for index,animal in enumerate(new_list):
    animal_dictionary.update({index: animal})
print(animal_dictionary)

    
