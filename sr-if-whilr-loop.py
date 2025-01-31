# Reset inventory for further examples
inventory = {"grapes": 7}

# While loop to sell grapes
while inventory["grapes"] > 0:
    print(f"Selling grapes. Remaining: {inventory['grapes']}")
    
    inventory["grapes"] -= 1  # Decrease stock of grapes by 1

    if inventory["grapes"] == 3:  # Check if stock is critically low
        print("Stopping sales, grapes stock is critically low.")
        break  # Stop selling if stock reaches 3
