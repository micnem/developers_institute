import json
from os import remove
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'menu'

def run_query(query, get_or_post = 'get'):
    connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    cursor =  connection.cursor()
    cursor.execute(query)
    if get_or_post == 'get':
        results = cursor.fetchall()
    else:
        connection.commit()
        results = None
    connection.close()
    return results
    

# class MenuManager:
#     def __init__(self, menu_path = 'menu.json'):
#         with open (menu_path, 'r') as f:
#             self.menu = json.load(f)
    
#     def add_item(self, name, price):
#         self.menu["items"].append({"name": name, "price": price})
#     def remove_item(self, name):
#         for i, item in enumerate(self.menu["items"]):
#             if name == item["name"]:
#                 del self.menu["items"][i] 
#             else:
#                 print("not in menu")
                
#     def save_to_file(self):
#         with open ('menu.json', 'w') as f:
#             self.menu =json.dump(self.menu,f)


class MenuItem:

    def __init__(self, name, price, id = 'default'):
        self.name = name
        self.price = price
        self.id = id

    def check_duplicates(self):
        pass

    def save(self):
        connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor =  connection.cursor()
        query = f"INSERT INTO menu_item (name, price) VALUES('{self.name}', {self.price})"
        cursor.execute(query)
        connection.commit()
        connection.close()
        # GET ID
        query = f"SELECT id from menu_item WHERE name = '{self.name}'"
        results = run_query(query)
        self.id = results[0][0]
        
    
    def update(self):

        query = f"UPDATE menu_item SET name = '{self.name}', price = {self.price} WHERE id = {self.id}"
        run_query(query, 'post')

    def delete(self):
        query = f"DELETE FROM menu_item WHERE id = {self.id}"
        run_query(query, 'post')
    
    @classmethod
    def all(cls):
        query = "SELECT * FROM menu_item"
        results = run_query(query)
        new_list = []
        for result in results:
            new_list.append(cls(result[0], result[1], result[2]))
            print(result[1], result[2])
        
        return new_list
       


        


# m1 = MenuManager()
# m1.add_item("Steak", 70)
# m1.add_item("Chips", 15)
# m1.save_to_file()

