def factorial(number):
    result = 1
    for digit in range(1,number +1):
        prod = digit*result
        result= prod
    return result
