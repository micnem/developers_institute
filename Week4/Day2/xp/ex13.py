users = ["Sam", "Jack", "Tom", "Julie"]

for i in users:
    age = int(input(f"{i}. How old are you? ")) 
    if age < 16:
        users.remove(i)

print(users)