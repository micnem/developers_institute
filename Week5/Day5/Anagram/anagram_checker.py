class AnagramChecker:
    def __init__(self):
        with open('anagrams.txt', 'r') as f:
            self.text_contents = f.read().lower().replace("\n"," ").split()
    
    def is_valid_word(self, word):
        if word not in self.text_contents:
            print("invalid word")
        else:
            print("valid Word")
    def is_anagram(self, word1, word2):

        if sorted(list(word1)) == sorted(list(word2)):
            return True
        return False

    def get_anagrams(self, user_word):
        anagrams = [word for word in self.text_contents if self.is_anagram(user_word, word)]
        return anagrams


