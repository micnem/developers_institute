class MenuManager:
    def __init__(self, menu):
        self.menu = menu
    def add_item(self, name, price, spice, gluten):
        item = {"name": name,
        "price": price,
        "spice": spice,
        "gluten": gluten}
        self.menu.append(item)
    def remove_item(self,name):
        item_names = [item["name"] for item in self.menu]
        if name not in item_names:
            print("this item is not on the menu")
        else:
            for item in self.menu:
                if item["name"] == name:
                    self.menu.remove(item)
    def update_item(self, name, price, spice, gluten):
        item_names = [item["name"] for item in self.menu]
        if name not in item_names:
            print("this item is not on the menu")
        else:
            for item in self.menu:
                if item["name"] == name:
                    self.menu.remove(item)
                    new_item = {"name": name,
                                "price": price,
                                 "spice": spice,
                                "gluten": gluten}
                    self.menu.append(new_item)
             
            
        

menu1 = MenuManager([])
menu1.add_item("Soup", 10, "B", False)
menu1.add_item("Hamburger", 15, "A", True)
menu1.add_item("Salad", 18, "A", False)
menu1.add_item("French Fries", 5, "C", False)
menu1.add_item("Beef bourguignon", 25, "B", True)
menu1.remove_item("Hamburger")
menu1.update_item("Salad", 18, "C", True)
print(menu1.menu)


