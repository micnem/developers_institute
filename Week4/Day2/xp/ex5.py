basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove(basket[-1])
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)
number_apples = basket.count("Apples")
print(number_apples)
basket.clear()
print(basket)