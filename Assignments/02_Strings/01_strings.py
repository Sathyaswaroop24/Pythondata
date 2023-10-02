"""
Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them. 
"""

first, last = input("Enter first and last name :").strip().split(' ')

print(first[::-1], last[::-1])