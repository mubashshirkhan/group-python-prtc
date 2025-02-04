inventory = {"apple": 10, "banana": 5, "orange": 8}
check_item = "banana"
new_item="kaju"

if new_item not in inventory:
    print(f"the {new_item} is not in the inventory")
elif check_item in inventory:
    print(f"Checking stock for {check_item}...")  # Corrected f-string syntax
    for _ in range(inventory[check_item]):  # Fixed loop syntax
        print(f"One {check_item} sold.")
