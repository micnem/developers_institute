def insert(element, mylist, index):
    new_list = []
    for item in mylist:
        if mylist.index(item)< index:
            new_list.append(item)
        elif mylist.index(item)== index:
            new_list.append(element)
            new_list.append(item)
        else:
            new_list.append(item)
    
    return new_list

        


    

