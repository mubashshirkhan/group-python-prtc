 #1. Check if a number is positive:
number = int(input("Enter a number: "))
while number <= 0:
    print("The number is not positive. Please enter a positive number.")
    number = int(input("Enter a number: "))
print("The number is positive!")

#2. Count down from 10 until 0
count = 10
while count >= 0:
    print(count)
    count -= 1

#3. Even number checker
number = int(input("Enter a number: "))
while number % 2 != 0:
    print("The number is not even. Please enter an even number.")
    number = int(input("Enter a number: "))
print("The number is even!")

#4. Sum numbers until a user enters 0
total = 0
number = int(input("Enter a number (or 0 to stop): "))
while number != 0:
    total += number
    number = int(input("Enter a number (or 0 to stop): "))
print(f"The total sum is {total}")

#5. Check if a number is a multiple of 5:
number = int(input("Enter a number: "))
while number % 5 != 0:
    print("The number is not a multiple of 5. Please enter another number.")
    number = int(input("Enter a number: "))
print("The number is a multiple of 5!")


#6. Guess the correct password:

password = "12345"
user_input = input("Enter the password: ")
while user_input != password:
    print("Incorrect password. Try again.")
    user_input = input("Enter the password: ")
print("Password correct!")
