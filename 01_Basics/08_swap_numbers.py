# ==========================================
# Program: Swap Two Numbers
# Description: Demonstrates swapping two numbers
#              using a temporary variable and
#              without a temporary variable.
# ==========================================

# Swapping using a temporary variable
print("Swapping Using a Temporary Variable")

a = 10
b = 20

print("Before Swapping:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("After Swapping:")
print("a =", a)
print("b =", b)

print()

# Swapping without a temporary variable
print("Swapping Without a Temporary Variable")

x = 30
y = 40

print("Before Swapping:")
print("x =", x)
print("y =", y)

x, y = y, x

print("After Swapping:")
print("x =", x)
print("y =", y)
