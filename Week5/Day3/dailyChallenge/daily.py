big_list = []
small_list =[]
for i in range(5):
    name = input("Input a name: ")
    small_list.append(name)
    age = input("Input age: ")
    small_list.append(age)
    score = input("Input a score: ")
    small_list.append(score)
    big_list.append(tuple(small_list))

print(big_list)
    

