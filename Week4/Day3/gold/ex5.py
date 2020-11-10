cars_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars_lst = cars_str.split(",")
print(f"there are {len(cars_lst)} manufacturers in the list")

print(sorted(cars_lst,reverse=True))

number_of_m = 0
number_of_not_i = 0
for car in cars_lst:
    if "i" in car == False:
        number_of_not_i += 1
    elif "M" in car:
        number_of_m += 1

print(f"There are/is {number_of_m} manufacturer with the letter M in it")
print(f"There are/is {number_of_not_i} manufacturer without the letter i in it.")
