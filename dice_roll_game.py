#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 07:36:34 2024

@author: robcary
"""
import random

def dice_roll(num_dice):
    while num_dice > 0:
        print("This die rolled a ",random.randint(1,6))
        num_dice -= 1
        
while True:
    str_dice = input("Enter a number of dice to roll (more than 1, less than 10): ")
    try:
        num_dice = int(str_dice)
    except:
        print("Invalid input, try again.")
        continue
    if num_dice < 1 or num_dice > 10:
        print("Too low/high, try again")
        continue
    dice_roll(num_dice)
    answer = input("Would you like to play again? (Y/N): ")
    if answer.upper() == "N":
        print("Thanks for playing!")
        raise SystemExit()
    elif answer.upper() == "Y":
        continue