def Show_menu(menu_dict):
    if not menu_dict:
        print("The menu is empty.")
    else:
        for drink, price in menu_dict.items():
            print(f"{drink} - {price}₪")

def Add_item(menu_dict):
    drink = input("Enter drink name: ")
    if drink in menu_dict:
        print("Item already exists!")
    else:
        price = input("Enter price: ")
        menu_dict[drink] = price
        print(f"{drink} added.")

def Update_price(menu_dict):
    drink = input("Enter drink name to update: ")
    if drink in menu_dict:
        new_price = input("Enter new price: ")
        menu_dict[drink] = new_price
        print("Price updated!")
    else:
        print("Item not found.")

def Delete_item(menu_dict):
    drink = input("Enter drink name to remove: ")
    if drink in menu_dict:
        del menu_dict[drink]
        print("Item deleted.")
    else:
        print("Item not found.")

def show_options():
    print("\nWhat would you like to do?")
    print("1. Show menu")
    print("2. Add item")
    print("3. Update price")
    print("4. Delete item")
    print("5. Exit")

def run_coffee_shop():
    menu = menu_dict = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}
    while True:
        show_options()
        choice = input("Choose option (1-5): ")
        
        if choice == '1':
            Show_menu(menu)
        elif choice == '2':
            Add_item(menu)
        elif choice == '3':
            Update_price(menu)
        elif choice == '4':
            Delete_item(menu)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

run_coffee_shop()