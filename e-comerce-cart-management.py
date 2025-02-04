import json
import os

CART_FILE = 'cart.json'

def load_cart():
    """Load cart data from JSON file"""
    if os.path.exists(CART_FILE):
        with open(CART_FILE, 'r') as file:
            return json.load(file)
    return {'cart': []}

def save_cart(cart):
    """Save cart data to JSON file"""
    with open(CART_FILE, 'w') as file:
        json.dump(cart, file, indent=4)

def add_item(cart):
    """Add item to cart"""
    item_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    # Check if item already exists in cart
    for item in cart['cart']:
        if item['id'] == item_id:
            item['quantity'] += quantity
            save_cart(cart)
            print(f"Updated quantity for {name}. New quantity: {item['quantity']}")
            return

    # Add new item
    new_item = {
        'id': item_id,
        'name': name,
        'price': price,
        'quantity': quantity
    }
    cart['cart'].append(new_item)
    save_cart(cart)
    print(f"{name} added to cart!")

def remove_item(cart):
    """Remove item from cart"""
    item_id = input("Enter product ID to remove: ")
    
    for index, item in enumerate(cart['cart']):
        if item['id'] == item_id:
            del cart['cart'][index]
            save_cart(cart)
            print(f"Item {item['name']} removed from cart!")
            return
    print("Item not found in cart.")

def view_cart(cart):
    """Display all items in cart"""
    if not cart['cart']:
        print("Your cart is empty!")
        return

    total = 0
    print("\nYour Shopping Cart:")
    print("{:<5} {:<20} {:<10} {:<10} {:<10}".format(
        "ID", "Name", "Price", "Quantity", "Total"))
    
    for item in cart['cart']:
        item_total = item['price'] * item['quantity']
        total += item_total
        print("{:<5} {:<20} ${:<9.2f} {:<10} ${:<10.2f}".format(
            item['id'],
            item['name'],
            item['price'],
            item['quantity'],
            item_total
        ))
    
    print("\nTotal: ${:.2f}".format(total))

def checkout(cart):
    """Process checkout and clear cart"""
    view_cart(cart)
    print("\nThank you for your purchase!")
    cart['cart'] = []
    save_cart(cart)
    exit()

def main():
    cart = load_cart()
    
    while True:
        print("\nE-commerce Cart System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_item(cart)
        elif choice == '2':
            remove_item(cart)
        elif choice == '3':
            view_cart(cart)
        elif choice == '4':
            checkout(cart)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()