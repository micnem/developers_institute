import anagram_checker

print("Welcome to anagram checker.")
def main():
    while True:
        user_word = input("Input a word (exit to quit): ")
        if user_word == "exit":
            break
        else:
            anagram_checker.get_anagrams(user_word)

main()