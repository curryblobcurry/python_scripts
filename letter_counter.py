#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:35:41 2024

@author: robcary
"""
# This program will accept a text file and will read through and count the number of letters
# that appear in the file (lowercase only), before printing out, in descending order, the letters found
# the most frequently.

import string

letter_count = {}
fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("Invalid file name")
    raise SystemExit()

# All these nested for loops are, first, going through each line of the file, then each
# word in each line, and finally each character of each word before checking if it's a lowercase
# letter or not.
for line in fhand:
    sentence = line.split()
    for word in sentence:
        for letter in word:
            # Maybe this is "cheating" but instead of attempting to group the characters NOT
            # acceptable, I imported the string module so I can call ascii_lowercase and
            # easily get a list of all lowercase letters.
            if letter in string.ascii_lowercase:
                letter_count[letter] = letter_count.get(letter,0) + 1
                
# This took me a minute to wrap my head around...before this step we have an unsorted dictionary
# of letters and their occurrence in a file. Per the problem statement, this needs to be sorted in
# descending order by occurrence, i.e. value.

# To do this, we call the sorted method and pass in the list of tuples in the dict via .items()
# and using the key parameter and a lambda function, sort on the values (the 2nd value in the tuples
# produced by .items(), and set reverse to True.)
sorted_letters = sorted(letter_count.items(), key = lambda x:x[1], reverse=True)

# This is still a list when printed, just FYI.
print(sorted_letters)

                