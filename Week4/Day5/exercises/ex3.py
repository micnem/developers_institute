def case_counter(sentence):
    upper_count = 0
    lower_count = 0
    sen_list = list(sentence)
    for character in sen_list:
        if ord(character)>64 and ord(character)<90:
            upper_count +=1
        elif ord(character)>96 and ord(character)<122:
            lower_count +=1
    return (f"Upper case characters: {upper_count}, lower case characters: {lower_count}")

