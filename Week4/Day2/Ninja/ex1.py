from math import sqrt
C = 50
H = 30
D = []
numbers = input("Input three numbers seperated by commas: ").split(",")
print(numbers)
answers = []

for number in numbers:
    answers.append(str(round(sqrt((2*C*int(number))/H))))

print(",".join(answers))


