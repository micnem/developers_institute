list1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
list2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
list3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
list4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

list5 = list1 + list2 + list3 + list4
print(list5)
sorted_lst = (sorted(list5, reverse=True))
print(sorted_lst)
print(sum(list5))

list6 = [list5[0] , list5[-1]]
print(list6)

list7 = []
for number in list5:
    if number>50:
        list7.append(number)

print(list7)
list8 = []
for number in list5:
    if number<10:
        list8.append(number)

print(list8)

list9 =[]
for number in list5:
    list9.append(number**2)
print(list9)

set1 = set(list5)
print(set1)
print(f"length of new set {len(set1)}")
print(f"length of old list {len(list5)}. Number of duplicates: {len(list5) - len(set1)}")


average = sum(list5)/len(list5)
print(f"average: {average}")

print(f"biggest number: {sorted_lst[0]}")
print(f"smallest number: {sorted_lst[-1]}")


sum_low_hi = sorted_lst[0]+sorted_lst[-1]
ave_low_hi = sum_low_hi/2
print(f"sum of lowest and highest number: {sum_low_hi}. Average is: {ave_low_hi}")

