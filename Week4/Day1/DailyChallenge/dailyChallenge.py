import random

text = input("Input a string (10 characters): ")
empty = ""
if len(text)<10:
    print("not long enough")
elif len(text)>10:
    print("toooo long")
else:
    # print(str[0:5])
    for i in range(len(text)):
        empty += text[i:i+1]
        print(empty)
        # first and last letters
        # print([text[1], text[-1]]) 
        
shuffled = ''.join(random.sample(text, len(text)))
print(f"this is your shuffled string: {shuffled}")
# import string_utils
# print(string_utils.shuffle(str))

# multi-line approach - cleaner
# text = list(text)
# random.shuffle(text)
# text = ''.join(text)