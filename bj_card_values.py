#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:09:06 2024

@author: robcary
"""
import re

def bj_values(card):
    if card.endswith("A"):
        return 1
    elif card.endswith("J") | card.endswith("Q") | card.endswith("K"):
        return 10
    elif re.search(r'\d+$',card):
        card_arr = re.findall(r'\d+$',card)
        return int(card_arr[0])