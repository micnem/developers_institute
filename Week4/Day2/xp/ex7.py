random_list = ["Giaccherini", "Romagnioli", "Donnarumma", "Maldini", "Ibrahimovic", "Gabbia"]

for person in random_list:
    if random_list.index(person) % 2 == 0 and random_list.index(person)!=0:
        print(person)