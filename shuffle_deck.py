#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 20:20:22 2024

@author: robcary
"""
from random import randrange

def shuffle_deck(deck):
    one = randrange(0,51);
    two = randrange(0,51);
    for i in range(1,500):
        if one!=two:
            temp = deck[one];
            deck[one] = deck[two];
            deck[two] = temp;
            one = randrange(0,51);
            two = randrange(0,51);
    return deck