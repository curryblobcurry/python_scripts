#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:00:14 2024

@author: robcary
"""
import card_methods
import bj_card_values

def blackjack(deck):
    player_hand = []
    player_hand.append(card_methods.draw(deck))
    player_hand.append(card_methods.draw(deck))
    the_house = []
    the_house.append(card_methods.draw(deck))
    the_house.append(card_methods.draw(deck))
    ptotal = 0
    htotal = 0
    for card in player_hand:
        ptotal += bj_card_values.bj_values(card)
    for card in the_house:
        htotal += bj_card_values.bj_values(card)
    


    print(f'Your Hand: {player_hand}, Total: {ptotal} ### The House: {the_house[0]}');
  #  next_move = input('Do you want to hit (H) or stay (S) ?');
  #  if next_move == 'H':
        
    return;
new_deck = card_methods.shuffle_deck(card_methods.init_deck())
blackjack(new_deck);
    