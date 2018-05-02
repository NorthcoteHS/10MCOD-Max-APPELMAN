"""
prog: circleCalculator.py
name: Max Appelman
date: 2018/03/12
desc: Calculates area and perimter of a circle.
"""
#displays welcome message
print('Welcome to the Circle Calculator!')

#asks user for the radius and converts to integer
r = input('Enter a radius: ')
r = int(r)

#calculates and prints area of a circle
area = 3.14 * r * r
print('The area is', area)

#calculates and prints perimeter of a circle
perimeter = 3.14 * r * 2
print('The perimeter is', perimeter)
