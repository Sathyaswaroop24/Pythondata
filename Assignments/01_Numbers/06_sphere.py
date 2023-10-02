"""
Write a Python program to get the volume of a sphere with radius six.
"""

# import libraries 
from math import pi


radius = float(input("Enter radius of sphere : ").strip())
print("Area of Sphere :",  ( 4 * pi * radius**3 ) / 3  )