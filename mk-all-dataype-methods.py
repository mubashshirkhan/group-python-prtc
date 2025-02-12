# String methods:-

first = "Hello World"

print(first.upper())
print(first.lower())
print(first.strip())
print(first.split())  # ['Hello', 'World']
print(first.replace("l", "j"))

# answers:-
# HELLO WORLD
# hello world
# Hello World
# ['Hello', 'World']
# Hejjo Worjd


# list methods:-

lst = [1, 2, 3, 4, 5, 5]
lst.append(8)
lst.insert(5, 10)
print(lst)
lst.remove(10)
print(lst)
print(lst.count(5))
lst.sort(reverse=False)
print(lst)
lst.reverse()
print(lst)
# lst.clear()
# del lst
print(lst)

# Answer
# [1, 2, 3, 4, 5, 10, 5, 8]
# [1, 2, 3, 4, 5, 5, 8]
# 2
# [1, 2, 3, 4, 5, 5, 8]
# [8, 5, 5, 4, 3, 2, 1]
# [8, 5, 5, 4, 3, 2, 1]

# dictionary methods:-

student_marks = {
    "math": "100",
    "phy": "80",
    "eng": "85",
    "com": "100"
}

print(student_marks.keys())
print(student_marks.items())
print(student_marks.values())
print(student_marks.get("phy"))
print(student_marks.pop("math"))
print(student_marks.popitem())
print(student_marks)
student_marks.clear()

# Answers
# dict_keys(['math', 'phy', 'eng', 'com'])
# dict_items([('math', '100'), ('phy', '80'), ('eng', '85'), ('com', '100')])
# dict_values(['100', '80', '85', '100'])
# 80
# 100
# ('com', '100')
# {'phy': '80', 'eng': '85'}

# Set methods:-

marks = {23, 3, 33, 56, 75}

clas = {23, 3, 33, 56, 75}
marks.add(55)
print(clas)
marks.remove(55)
print(clas)
marks.discard(3)
print(clas)
marks.pop()
print(clas)
marks.clear()
print(clas)
marks.update(clas)
print(clas)
print(marks)

# answers:-
# {33, 3, 23, 56, 75}
# {33, 3, 23, 56, 75}
# {33, 3, 23, 56, 75}
# {33, 3, 23, 56, 75}
# {33, 3, 23, 56, 75}
# {33, 3, 23, 56, 75}
# {33, 3, 23, 56, 75}
