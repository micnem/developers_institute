import random
temp = 0
season_input = input("Is it Summer or Winter? ")
def get_random_temp(season):
    if season == "Winter":
         temp = random.randrange(-10, 16) 
    elif season == "Summer":
        temp = random.randrange(17, 40) 
    return temp


def main():
    rand_temp = get_random_temp(season_input)
    print(f"the temp outside is {rand_temp}")
    if rand_temp>0 and rand_temp<=16:
        print("It's cold, don't forget your coat!")
    elif rand_temp<=0:
        print("It's freezing!")
    elif rand_temp>16 and rand_temp<=23:
        print("It's a bit chilly")
    elif rand_temp>23 and rand_temp<=32:
        print("It's a perfect day")
    elif rand_temp>32:
        print("It is super hot!")


main()