def space_counter(sentence):
    counter = 0
    sen_list = list(sentence)
    for character in sen_list:
        if character.isalnum():
            continue
        else:
            counter +=1
    return counter


