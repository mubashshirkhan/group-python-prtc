#2. Nesting while loop: Managing multiple inventory items
inventory = {"apple": 10, "banana": 5, "orange": 8}

item_names = list(inventory.keys())  # Corrected syntax

index = 0  # Initialized index

while index < len(item_names):  # Loop through item names
    item = item_names[index]  # Assign current item

    while inventory[item] > 0:  # Ensure condition is correct
        print(f"Selling a {item}. Remaining: {inventory[item] - 1}")
        inventory[item] -= 1

    print(f"{item.capitalize()} is out of stock!\n")  # Corrected f-string syntax
    index += 1  # Increment index
