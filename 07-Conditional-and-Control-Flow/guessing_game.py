#!/usr/bin/env python3

"""
	__author__ 	: codelocked
	__date__	: Since September 2023
	__desc__	: Guessing Game

"""

import random

print("WELCOME TO GUESSING GAME")

while True:
	guess = str(input("Enter H for HEAD and T to see the your guess : ").upper())
	if guess not in ('H','T'):
		guess = str(input("Enter H for HEAD and T to see the your guess : ").upper())
	random_list = ["H","T"]
	if random.choice(random_list) == guess:
		print("Congratulation! your guess is correct")
		break
	else:
		print("Better luck next time...")
		cont = str(input("Do you want to try again [y/N] : "))
		if cont in ["y","Y"]:
			continue
		else:
			break
