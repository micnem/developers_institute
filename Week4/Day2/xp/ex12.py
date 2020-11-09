# price = 0
# while True:
#     user_input = input("What is your age? ")
#     if user_input == "quit":
#         print(price)
#         break
#     else:
#         age = int(user_input)
#         if age>3 and age <12:
#             price += 10
#         elif age >= 12:
#             price += 15
name = ""
group = []
price = 0
while True:
        user_input = input(f"User. What is your age? ")
        if user_input == "quit":
            print(f"{group} can see the movie. Bye")
            break
        else:
            age = int(user_input)
            if age>16 and age <21:
                print("you can see the movie")
                name = input("what is your name? ")
                group.append(name)
            else:
                print("you cannot see the movie")
