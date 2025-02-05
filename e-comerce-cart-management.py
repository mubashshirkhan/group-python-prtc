
import json

# Create a dictionary of electronic products and their prices
electronic_products = {
    "laptop": 999.99,
    "mouse": 19.99,
    "keyboard": 49.95,
    "monitor": 149.99,
    "headphones": 79.50,
    "printer": 129.00,
    "usb drive": 12.99,
    "external hard drive": 89.99,
    "tablet": 299.00,
    "router": 59.95
}

# Initialize shopping cart
shopping_cart = []

def display_products():
    print("\nAvailable Products:")
    for product, price in electronic_products.items():
        print(f"{product.capitalize():<20} ${price:.2f}")

def add_to_cart(product_name):
    product_name = product_name.lower()
    if product_name in electronic_products:
        # Check if product already exists in cart
        for item in shopping_cart:
            if item["product"] == product_name:
                item["quantity"] += 1
                return
        # Add new product to cart
        shopping_cart.append({
            "product": product_name,
            "price": electronic_products[product_name],
            "quantity": 1
        })
    else:
        print("Product not found!")

def save_cart_to_json():
    with open("shopping_cart.json", "w") as file:
        json.dump(shopping_cart, file, indent=4)
    print("\nCart saved to shopping_cart.json")

def main():
    print("Welcome to the Electronics Store!")
    display_products()
    
    while True:
        print("\nEnter product name to add to cart (or 'done' to finish, 'list' to show products)")
        choice = input("Your choice: ").strip().lower()
        
        if choice == 'done':
            break
        elif choice == 'list':
            display_products()
        else:
            add_to_cart(choice)
            print(f"Added {choice} to cart")
    
    # Save cart to JSON file
    if shopping_cart:
        save_cart_to_json()
        print("\nFinal Cart Contents:")
        total = 0
        for item in shopping_cart:
            item_total = item["price"] * item["quantity"]
            total += item_total
            print(f"{item['product'].capitalize()} x{item['quantity']}: ${item_total:.2f}")
        print(f"\nTotal Amount: ${total:.2f}")
    else:
        print("\nYour cart is empty. No items to save.")

if __name__ == "__main__":
    main()