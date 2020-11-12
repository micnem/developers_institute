import random
def  throw_dice():
    result = random.randrange(1, 7)
    return result


def throw_until_doubles():
    number_of_rolls = 0
    result1 =0
    result2=1
    palying = True
    if result2 == result1:
        playing = False
    else:
        result1 = throw_dice()
        result2 = throw_dice()
        number_of_rolls += 1
    return number_of_rolls
       

print(throw_until_doubles())

