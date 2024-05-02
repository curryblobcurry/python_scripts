#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:54:44 2024

@author: robcary
"""

def init_deck():
    deck = [];
    suit = "";
    card = "";
    for i in range(1,5):
        match i:
            case 1:
                suit = "H";
            case 2:
                suit = "C";
            case 3:
                suit = "D";
            case 4:
                suit = "S";
        for j in range(1,14):
            match j:
                case 1:
                    card = "A"
                    deck.append(suit + card);
                case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10:
                    card = str(j)
                    deck.append(suit + card);
                case 11:
                    card = "J"
                    deck.append(suit + card);
                case 12:
                    card = "Q"
                    deck.append(suit + card);
                case 13:
                    card = "K"
                    deck.append(suit + card);
    return deck