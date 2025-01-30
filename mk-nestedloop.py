# Example 1: Nested for loop
for i in range(3):
    for j in range(3):
        print(f"i = {i}, j = {j}")

# Example 2: Nested while loop
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1

# Example 3: Nested loop with list comprehension
matrix = [[i * j for j in range(3)] for i in range(3)]
for row in matrix:
    print(row)