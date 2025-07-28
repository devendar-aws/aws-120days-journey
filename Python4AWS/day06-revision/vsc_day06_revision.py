inventory = {
    "Apple": 10,
    "Banana": 20,
    "Mango": 15
}
def add_stock(stock, fruit, quantity):
    if fruit in stock:
        stock[fruit] += quantity
    else:
        print(stock)
    return stock
def sell_fruit(stock, fruit, quantity):
    if fruit in stock:
        if stock[fruit] >= quantity:
            stock[fruit] -= quantity
        else:
            print("Not enough stock")
    else:
        print("Item not found")
    return stock

updated = add_stock(inventory, "Apple", 5)
updated = sell_fruit(inventory, "Banana", 3)
inventory = updated
print(inventory)


# ✅ Inventory Tracker Loop (add/sell/show/exit)
def add_fruit(stock, fruit, quantity):
    stock[fruit] = stock.get(fruit, 0) + quantity
    print(f"{fruit} added. Current stock: {stock[fruit]} kg")

def sell_fruit(stock, fruit, quantity):
    if fruit in stock:
        if stock[fruit] >= quantity:
            stock[fruit] -= quantity
            print(f"{fruit} sold. Remaining stock: {stock[fruit]} kg")
        else:
            print("Not enough stock")
    else:
        print("Item not found")
        
def show_inventory(stock):
    if not stock:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for fruit, qty in stock.items():
            print(f"{fruit}: {qty} kg")

# Main Inventory Tracker Loop
Inv_Tracker = {}

while True:
    action = input("What do you want to do? (add/sell/show/exit): ").strip().lower()
    
    if action == "add":
        fruit = input("Enter fruit name: ").capitalize()
        quantity = int(input("Enter quantity in kg: "))
        add_fruit(Inv_Tracker, fruit, quantity)
        
    elif action == "sell":
        fruit = input("Enter fruit name: ").capitalize()
        quantity = int(input("Enter quantity in kg: "))
        sell_fruit(Inv_Tracker, fruit, quantity)
        
    elif action == "show":
        show_inventory(Inv_Tracker)
        
    elif action == "exit":
        print("Exiting Inventory Tracker. Goodbye!")
        break
        
    else:
        print("Invalid action. Please choose add/sell/show/exit.")
