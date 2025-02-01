inventory = {"apple": 10, "banana": 5, "orange": 8}
for fruit, stock in inventory.items():
    if stock < 6:  # Proper indentation
        print(f"Warning: Low stock of {fruit} ({stock} remaining)")  # Fixed f-string syntax
        break
