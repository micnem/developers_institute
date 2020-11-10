birthdays = {
    "Alfred": "1997/04/28",
    "Ben": "2003/06/13",
    "Colin": "2000/03/19",
    "Donald": "1948/04/12",
    "Edwin": "1902/12/30"
}
print(list(birthdays.keys()))

name = input("Welcome! Type in someone's name to find out their birthday: ")
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"{name} is not in the list")

