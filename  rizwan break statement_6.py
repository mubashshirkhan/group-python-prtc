#6.break statement: stop selling if reaches a threshold
inventory = {"apple":10,"banana":5,"orange":8}
inventory = {"grapes": 7}
while inventory["grapes"] > 0:
    print(f"selling grapes. remaining: {inventory['grapes']}")
    inventory["grapes"] -= 1
    if inventory["grapes"] == 3:
        print("stopping sales, grapes stock is critically low.")
        break
    