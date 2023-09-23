#!/usr/bin/env python3

"""
	__author__ 	: codelocked
	__date__	: Since September 2023
	__desc__	: Even Number

"""

numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
	if num % 2 == 0:
		print("First Even Number found!")
		break
else:
	print('the list doesnot contain even number') 
 
