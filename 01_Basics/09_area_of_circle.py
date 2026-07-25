# ==========================================
# Program: Area of a Circle
# Description: Calculates the area of a circle
#              using the radius entered by the user.
# ==========================================

import math

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = math.pi * radius ** 2

# Display the result
print("\nArea of the Circle =", round(area, 2))
