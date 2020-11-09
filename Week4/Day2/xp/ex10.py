fave_fruits = input("add your favourite fruits (seperated by space): ").lower()
fave_list = fave_fruits.split()
print(fave_list)

checker = input("what fruit are you eating right now? ").lower()

if checker in fave_list:
    print("enjoy one of your favourite fruits!")
else:
    print("I hope you like it anyway!")