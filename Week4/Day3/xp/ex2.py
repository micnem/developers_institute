family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
family_and_cost ={}
price = 0
fare = 0
for person in family:
    if family[person] >= 3 and family[person]<=12:
        fare = 10
        price+=10
        print(f"Name: {person} --- fare: {fare}")
    elif family[person]<3:
        price +=0
    else:
        fare = 15
        price+=15
        print(f"Name: {person} --- fare: {fare}")


print(f"total cost: {price}")
