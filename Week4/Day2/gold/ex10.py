receipt = []
name = input("Customer's name: ")
print("Name added")
receipt.append(f"Customer: {name}")

waiter_name = input("Waiter's name: ")
print("waiter added")
receipt.append(f"Waiter: {waiter_name}")

item = input("item: ")
print("item added")
receipt.append(f"item: {item}")

price = int(input("price: "))
receipt.append(f"Item price: {price}")

quant = int(input("Quantity ordered: "))
receipt.append(f"Quantity: {quant}")

disc = int(input("Discount: "))

total = (price*quant) - disc
vat_total = (0.2*price) + price

receipt.append(f"price: {vat_total}")

print('\n'.join(receipt))



