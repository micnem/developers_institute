import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'rush', 'south']
word = random.choice(wordslist) 


guessed_letters = []
incorrect_letters = []
def obfuscate():
    obfuscated=[]
    for letter in word:
        if letter not in guessed_letters:
            obfuscated.append("_")
        else:
            obfuscated.append(letter)
    return obfuscated

def guesser():
    obfuscated = obfuscate()
    print(obfuscated)
    guess = input("input a letter: ")
    if guess in guessed_letters:
        print("You have already guessed that letter, try again")
    elif word.find(guess)==-1:
        if guess in incorrect_letters:
            print(f"letter already guessed (incorrect). Letters already guessed: {incorrect_letters}")
        
        else:
            print("You guessed wrong")
            incorrect_letters.append(guess)
            print(f"you have {6 - len(incorrect_letters)} lives remaining. Letters already guessed: {incorrect_letters}")
    else:
        guessed_letters.append(guess)
        print("you guessed right")
        print(f"Wrong letters guessed: {incorrect_letters}")
    
    
while len(incorrect_letters) <6:
    guesser()

