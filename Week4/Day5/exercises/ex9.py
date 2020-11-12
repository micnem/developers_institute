def isMono(mylist):
    new_list = sorted(mylist)
    rev_list = sorted(mylist, reverse=True)
    if mylist == new_list or mylist==rev_list:
        return True
    else:
        return False
