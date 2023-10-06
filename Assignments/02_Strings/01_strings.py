"""
Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them. 
"""

first, last = input("Enter first and last name :").strip().split(' ')

print(first[::-1], last[::-1])


# Program to accept first and last name of user and print them in reverse order

firstName=input("Enter your First name  :  ")
lastName = input(" Enter your last name :   ")

reverseString=firstName[::-1] + '  ' + lastName[::-1]
print(reverseString)