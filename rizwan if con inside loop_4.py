#4.if conditional statement inside for loop
inventory = {"apple":10,"banana":5,"orange":8}
for fruit,stock in inventory.items():
    if stock < 6:
        print(f"warning: Low stock of {fruit} ({stock} remaining.")