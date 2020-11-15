class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
def find_oldest(cat_list):
    oldest_cat = cat_list[0]

    for cat in cat_list:
        if cat.age > oldest_cat.age:
            oldest_cat = cat

    return oldest_cat


cat1 = Cat("Tommy", 3)
cat2 = Cat("Jon", 4)
cat3 = Cat("Mike", 5)

cat_list = [cat1,cat2,cat3]

oldest_cat = find_oldest(cat_list)

print(f"The oldest cat is {oldest_cat.name}. He/She is {oldest_cat.age} years old.")
