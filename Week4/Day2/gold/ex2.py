numbers = []
while len(numbers)<3:
    user_input = int(input("input a number: "))
    numbers.append(user_input)

numbers.sort()
print(f"the greatest number is: {numbers[-1]}")
