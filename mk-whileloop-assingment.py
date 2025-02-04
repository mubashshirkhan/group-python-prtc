
count = 0
while count < 5:
    print("Count is:", count)
    count += 1



count = 0
while True:
    print("Count is:", count)
    count += 1
    if count >= 5:
        break



count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print("Odd count is:", count)




count = 0
while count < 5:
    print("Count is:", count)
    count += 1
else:
    print("Loop ended with count:", count)




outer_count = 0
while outer_count < 3:
    inner_count = 0
    while inner_count < 3:
        print(f"Outer count: {outer_count}, Inner count: {inner_count}")
        inner_count += 1
    outer_count += 1



while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input.lower() == 'exit':
        print("Exiting loop.")
        break
    else:
        print("You entered:", user_input)