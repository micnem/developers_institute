words = input("Input seven words seperated by space: ").split()
letter = input("type in a letter: ")

for i in words:
    if letter in i:
        print(f"Word index: {words.index(i)}")
        print(f"Letter index: {i.index(letter)}")
    else:
        continue
