
count = 0
while count < 6:
    print("Count is 1st:", count)
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
        print(inner_count, "inner_count")
    outer_count += 1
    print(outer_count, "outer_count")



'''This Python program consists of a nested loop structure, where an outer while loop controls an inner while loop.

Breakdown of the Code Execution:
The outer_count variable starts at 0.
The outer while loop runs while outer_count < 3.
Inside the outer loop:
The inner_count variable is initialized to 0 for each iteration of outer_count.
The inner while loop runs while inner_count < 3.
In each iteration of the inner loop:
It prints the values of outer_count and inner_count.
inner_count is incremented by 1.
It prints the updated inner_count value.
When inner_count reaches 3, the inner loop ends.
After exiting the inner loop, outer_count is incremented by 1.
The updated outer_count value is printed.
The process repeats until outer_count reaches 3, at which point the program terminates.'''



while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input.lower() == 'exit':
        print("Exiting loop.")
        break
    else:
        print("You entered:", user_input)
