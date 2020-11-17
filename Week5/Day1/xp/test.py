animals = ["Ape", "Cat", "Bear", "Cougar", "Baboon", "Eel", "Emu", "Bat"]
animals = sorted(animals)
sorted_animals = {}
key = 1
starting_letter = animals[0][0]   #A
for animal in animals:
	#check starting letter
	if animal[0] != starting_letter:
		key += 1
		starting_letter = animal[0]
	if key not in sorted_animals:
		sorted_animals[key] = animal
	else:  
		if not isinstance(sorted_animals[key], list):
			sorted_animals[key] = [sorted_animals[key]]
		sorted_animals[key].append(animal)
print(sorted_animals)
# {
# 	1: 'Ape', 
# 	2: ['Baboon', 'Bat', 'Bear'], 
# 	3: ['Cat', 'Cougar'], 
# 	4: ['Eel', 'Emu']
# }