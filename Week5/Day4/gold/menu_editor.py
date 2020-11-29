import menu_manager

def load_manager():
    menu_manager.MenuManager()
def show_user_menu():
    selection = input("Welcome to MenuManagerPro.\n(a) Add an item \n(b) Delete an item \n(v) View the menu\n(x) Exit\n: ").lower()
    if selection == "a":
        add_item_to_menu()
    elif selection == "b":
        remove_item_from_menu()
    elif selection == "v":
        show_restaurant_menu()

def add_item_to_menu():
    item = menu_manager.MenuItem(input("Input item name followed by price: "))
    item.menu_manager.MenuItem.save()
    

def remove_item_from_menu():
    pass
def show_restaurant_menu():
    pass

show_user_menu()