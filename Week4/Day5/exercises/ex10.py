def longest(mylist):
    longest_word = mylist[0]
    for word in mylist:
        if len(word)>len(longest_word):
            longest_word=word
    return longest_word


