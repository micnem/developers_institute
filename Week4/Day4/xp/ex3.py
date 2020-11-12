def adder(number):
    list1 =[]
    number_str = str(number)
    for i in range(1,5):
        list1.append(int(number_str * i))

    return sum(list1)

    
    
print(adder(3))
