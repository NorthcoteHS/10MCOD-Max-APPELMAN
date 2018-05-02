"""
Prog:   rectangleCalculator.py
Name:   Max Appelman
Date:   2018/03/12
Desc:   Calculates the area and perimeter of a rectangle.
"""

# Display welcome message.
print('Welcome to the Rectangle Calculator!')

# Use input to get the rectangle's length and width
length=input("Enter the length: ")
width=input("Enter the width: ")

# Convert length and width to integers.
length = int(length)
width = int(width)

# Calculate the area
area = length*width

# Display the area.
print('The area is', area)

# Calculate and display the perimeter
perimeter = 2*length + 2*width
print('the perimeter is', perimeter)
