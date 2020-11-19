import random 

def get_words_from_file():
    with open('random_words.txt', "r") as f:
        words_in_list = [word.strip() for word in f.readlines()]
    return words_in_list
def get_random_sentence(length):
    words = get_words_from_file()
    sentence = random.sample(words, length)
    sentence = " ".join(sentence)
    print(sentence.title())
def main():
    user_input = int(input("Input a number and a sentence with that number of words will be returned: "))
    if not 2 <= user_input <= 20:
	    raise ValueError('number out of range') 
    print(get_random_sentence(user_input))  


main()
