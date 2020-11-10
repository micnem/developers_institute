items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}



for item in items:
    items[item]=[items[item], 5]

print(items)


total_value = 0

for item in items:
    total_value += items[item][0]*items[item][1]
    

print(f"the value of all of the items is: {total_value}")