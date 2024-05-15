#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:57:03 2024

@author: robcary
"""
from random import randrange

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
                    deck.append(suit+card)
                case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10:
                    card = str(j)
                    deck.append(suit+card);
                case 11:
                    card = "J"
                    deck.append(suit+card);
                case 12:
                    card = "Q"
                    deck.append(suit+card);
                case 13:
                    card = "K"
                    deck.append(suit+card);
    return deck

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

def draw(deck):
    return deck.pop()