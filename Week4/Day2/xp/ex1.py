my_fav_numbers = {2, 234, 9}
new_numbers = {1,4}
my_fav_numbers.update(new_numbers)
my_fav_numbers.pop()
print(my_fav_numbers)

friend_fav_numbers = {7,34,90,69}

our_fav_numbers = friend_fav_numbers.union(my_fav_numbers)
print(our_fav_numbers)