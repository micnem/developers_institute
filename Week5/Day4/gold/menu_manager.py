import json
from os import remove
class MenuManager:
    def __init__(self, menu_path = 'menu.json'):
        with open (menu_path, 'r') as f:
            self.menu = json.load(f)
    
    def add_item(self, name, price):
        self.menu["items"].append({"name": name, "price": price})
    def remove_item(self, name):
        for i, item in enumerate(self.menu["items"]):
            if name == item["name"]:
                del self.menu["items"][i] 
            else:
                print("not in menu")
                
    def save_to_file(self):
        with open ('menu.json', 'w') as f:
            self.menu =json.dump(self.menu,f)


m1 = MenuManager()
m1.add_item("Steak", 70)
m1.add_item("Chips", 15)
m1.save_to_file()

