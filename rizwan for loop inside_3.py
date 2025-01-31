#3. for loop inside if conditional statement
inventory = {"apple":10,"banana":5,"orange":8}
check_item = "banana"
if check_item in inventory:
    print(f"checking stock for {check_item},,,")
    for _ in range(inventory[check_item]):
        print(f"one {check_item} sold.")