# ==========================================
# Program: Operators in Python
# Description: Demonstrates different types of operators in Python.
# ==========================================

a = 20
b = 10

# Arithmetic Operators
print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

print()

# Comparison Operators
print("Comparison Operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print()

# Logical Operators
print("Logical Operators")
x = True
y = False

print("x and y :", x and y)
print("x or y  :", x or y)
print("not x   :", not x)

print()

# Assignment Operators
print("Assignment Operators")
c = 5
print("Initial Value:", c)

c += 2
print("After += :", c)

c -= 1
print("After -= :", c)

c *= 3
print("After *= :", c)

print()

# Membership Operators
print("Membership Operators")
fruits = ["Apple", "Banana", "Mango"]

print("'Apple' in fruits :", "Apple" in fruits)
print("'Orange' not in fruits :", "Orange" not in fruits)

print()

# Identity Operators
print("Identity Operators")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)
print("list1 == list3 :", list1 == list3)
