inventory = {"apple": 10, "banana": 5, "orange": 8}

fruit = "orange"  # Corrected variable assignment

while inventory[fruit] > 0:  # Fixed condition syntax
    if inventory[fruit] == 3:  # Changed 35 to a more reasonable low-stock number
        print(f"Stock of {fruit} is critically low ({inventory[fruit]} left).")  # Fixed f-string syntax

    print(f"Selling an {fruit}. Remaining: {inventory[fruit] - 1}")  # Fixed f-string syntax

    inventory[fruit] -= 1  # Fixed decrement operator

print(f"{fruit.capitalize()} is out of stock!\n")  # Fixed f-string syntax
