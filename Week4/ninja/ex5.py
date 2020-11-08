sen = input("Input a sentence without the letter a in it: ")
length = len(sen)
active = True
newSen = ""
if ("a" in sen):
    active = False
    print("sorry, your sentence has an a in it")


while active:

    newSen = input("input another sentence: ")
    newLen = len(newSen)
    if newLen>length:
        hiScore = newLen
        print("new highscore", hiScore)
    else:
        print("that was shorter, try again")
        input("Input another sentence: ")
        
    