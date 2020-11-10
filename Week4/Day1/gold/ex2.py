input = input("input a month represented by its number: ")
input_toInt = int(input)

if(input_toInt>=3 and input_toInt<=6):
    print("spring")

elif (input_toInt>6 and input_toInt<=8):
    print("It's Summer!")

elif(input_toInt>=9 and input_toInt<11):
    print("autumn")

else:
    print("brr its winter")
