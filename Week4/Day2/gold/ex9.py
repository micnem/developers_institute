import random
while True:
    user_number = int(input("Guess a number between 1-9: "))
    comp_number = random.randint(1,9)

    if user_number==comp_number:
        print("congrats u won")
    else:
        print(f"Wrong. Number was {comp_number}")
    
    