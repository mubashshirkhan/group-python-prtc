inventory = {"apple": 10, "banana": 5, "orange": 8}

inventory = {"grapes": 7}  # Fixed dictionary assignment

while inventory["grapes"] > 0:  # Corrected syntax
    print(f"Selling grapes. Remaining: {inventory['grapes'] - 1}")  # Fixed f-string syntax

    inventory["grapes"] -= 1  # Fixed decrement operation

    if inventory["grapes"] == 3:
        print("Stopping sales, grapes stock is critically low.")  # Fixed capitalization
        break
