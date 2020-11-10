users = ["Sam", "Jack", "Tom", "Julie"]
users2 = []
for i in users:
    age = int(input(f"{i}. How old are you? ")) 
    if age < 16:
        users2.append(i)

print(users2)