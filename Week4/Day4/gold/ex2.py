import random
playing = True
def throw_dice():
    result1 = random.randrange(1, 7)
    result2 = random.randrange(1, 7)
    return result1, result2

# while playing:
#     print(throw_dice())
def throw_until_doubles():

    throw_dice()
    counter+=1
    if result1 == result2:
        break
    return counter


print(throw_until_doubles())