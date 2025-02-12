age = 22
meassge = "Eligible "if age >= 18 else "Not eligible"
print(meassge)


high_income = True
good_credit = True
student = False

if not student:
    print("Eligible")
else:
    print("not eligible")

high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("not eligble")


age = 16

if 18 <= age < 65:
    print("eligible")
else:
    print("not")


for x in range(1, 6, 2):
    print("Attempt", x, x*".")


successful = False

for number in range(3):
    print("Attempt")
    if successful:
        print("succesfull")
        break
else:
    print("you have attempted 4 times, attempt failed")


for x in range(5):
    for y in range(3):
        print(f"({x},{y})")


number = 100

while number > 0:
    print(number)
    number //= 2


command = ""

while command.lower() != "quit":
    command = input(":=")
    print("Echo", command)
