newSen = ""
hi_score = 0
while True:
    sen = input("Input a sentence without the letter a in it: ")
    if "a" in sen:
        print("sorry, your sentence has an a in it")
        continue
    else:
        if len(sen)>hi_score:
            hi_score = len(sen)
            print(f"new high score of {hi_score}")
        
    