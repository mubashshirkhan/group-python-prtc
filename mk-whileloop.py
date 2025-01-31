inventory={"apple": 10, "banana": 5, "orange": 8}

#1. While loop: Decrease inventory until it's empty

while inventory["apple"] > 0:

    print(f"Selling an apple. Remaining: (inventory['apple'])")

    inventory["apple"] -- 1

print("Apples are out of stock!\n")
