str = input("Input a string (10 characters): ")
empty = ""
if(len(str)<10):
    print("not long enough")
elif(len(str)>10):
    print("toooo long")
else:
    # print(str[0:5])
    for i in range(len(str)):
        empty += str[i:i+1]
        print(empty)
        
import string_utils
print(string_utils.shuffle(str))
