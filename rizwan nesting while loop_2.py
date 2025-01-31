# 2. nesting  while loop: managing multiple inventory items

inventory = {"apple":10,"banana":5,"orange":8}
item_name = list(inventory.keys())
index = 0
while index < len(item_name):
    item = item_name[index]
    while inventory[item] > 0:
        print(f"salling a {item}. remaining: {inventory[item]}")
        inventory[item] -= 1
        print(f"{item.capitalize()} is out of stock!\n")
        index += 1