def max_list(mylist):
    biggest = mylist[0]
    for number in mylist:
        if number>biggest:
            biggest = number
    return biggest

