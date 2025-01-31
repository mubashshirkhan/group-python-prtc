#5. if coinditional statement inside while loop.
inventory = {"apple":10,"banana":5,"orange":8}
fruit = "orange"
while inventory[fruit] > 0:
    if inventory[fruit] == 3:
        print(f"stock of {fruit} is critically low ({inventory[fruit]})")
        print(f"selling an {fruit}. remaining {inventory[fruit]}")
        inventory[fruit] -= 1