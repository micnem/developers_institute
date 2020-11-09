pizza = []
price = 10
while True:
    topping = input("add a topping: ")
    if topping == "quit":
        print(f"your pizza has {pizza} and costs {price}")
        break
    else:
        price += 2.5
        print(f"{topping} is being added")
        pizza.append(topping)