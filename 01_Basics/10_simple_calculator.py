# ==========================================
# Program: Simple Calculator
# Description: Performs basic arithmetic
#              operations based on user choice.
# ==========================================

# Get input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("\nSelect an Operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("\nResult =", number1 + number2)

elif choice == "2":
    print("\nResult =", number1 - number2)

elif choice == "3":
    print("\nResult =", number1 * number2)

elif choice == "4":
    if number2 != 0:
        print("\nResult =", number1 / number2)
    else:
        print("\nError: Division by zero is not allowed.")

else:
    print("\nInvalid choice. Please select a number between 1 and 4.")
