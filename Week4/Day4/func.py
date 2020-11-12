# def sum_list(mylist):
#     total =  0
#     for number in mylist:
#         total+=number
#     return total

# print(sum_list([1,2,3]))


# def min_list(mylist):
#     first = mylist[0]
#     for number in mylist:
#         if number<first:
#             first = number
#     return first


# print(min_list([-4,-783,-100]))
            
def max_list(mylist):
    biggest = mylist[0]
    for number in mylist:
        if number>biggest:
            biggest = number
    return biggest

print(max_list([-4,-783,-100]))


