"""
    Description:  Write a Python program to get the calculate area of Circle.
"""

__author__ = 'Code Locked'
__version__ = '1.0.0'

# Import labaries
from math import pi


radius = float(input("Enter radius for which you want Area of Circle : ").strip())
print(f"Area of Circle wiht radius {radius} cm is { pi*radius**2 } cm2")
