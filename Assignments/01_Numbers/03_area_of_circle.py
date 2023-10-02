"""
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

# import libraries
from math import pi

radius = float(input("Enter radius value :").strip())
area = pi * radius ** 2
print("Area of Circle : ", area )