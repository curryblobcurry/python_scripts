#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:00:14 2024

@author: robcary
"""
import init_deck
import shuffle_deck

def blackjack(deck):
    player_hand = [];
    the_house = [];
    player_hand.append(deck[0]);
    deck.pop(0);
    the_house.append(deck[1]);
    deck.pop(1);
    player_hand.append(deck[2]);
    deck.pop(2);
    print(f'Your Hand: {player_hand} ### The House: {the_house[0]}');
    next_move = input('Do you want to hit (H) or stay (S) ?');
    if next_move == 'H':
        
    return;
new_deck = shuffle_deck.shuffle_deck(init_deck.init_deck())
blackjack(new_deck);
    