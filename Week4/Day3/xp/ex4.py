users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
values = [0,1,2,3,4]
disney_users_B = enumerate(users)
disney_users_A = {}

print(dict(disney_users_B))

disney_users_A = dict(zip(users, values))
print(disney_users_A)


disney_users_C = dict(zip(sorted(users), values))
print(disney_users_C)

users2 = []

for user in users:
    if "i" in user and user.startswith("M"):
        users2.append(user)

values2 = range(len(users2))
disney_users_D = dict(zip(users2, values2))
print(disney_users_D)

