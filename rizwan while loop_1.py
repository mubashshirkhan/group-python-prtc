#1 while loop decrease inventory until it's empty 
invevtory = {"apple":10,"banana":5,"orange":8}
while inventory["apple"] > 0:
    print(f"selling an apple. remaining: {inventory["apple"]}")
    inventory["apple"] -= 1
    print("apples are out of stock!\n")