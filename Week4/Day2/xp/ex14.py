family = []
while True:
    selection = int(input("Select a number 1 - 4: "))

    if selection == 1:
        new_name = input("add a name: ")
        family.append(new_name)
    elif selection == 2:
        rem_name = input("Who do you want to remove? ")
        family.remove(rem_name)
    elif selection == 3:
        print(family)

    elif selection == 4:
        break
    else:
        print("Invalid number entered")

