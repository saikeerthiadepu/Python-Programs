# Program: Type Casting in Python
# Description: Demonstrates implicit and explicit type casting.

# Implicit Type Casting
integer_number = 10
float_number = 5.5

result = integer_number + float_number

print("Implicit Type Casting")
print("Result:", result)
print("Data Type:", type(result))

print()

# Explicit Type Casting
number = "100"

converted_integer = int(number)
converted_float = float(number)
converted_string = str(converted_integer)

print("Explicit Type Casting")
print("Integer:", converted_integer)
print("Float:", converted_float)
print("String:", converted_string)
