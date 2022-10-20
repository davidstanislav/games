# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:56:47 2022

@author: djstanis
"""

import numpy as np
import random

def create_board():
    number_tiles = [4, 5, 6, 8, 9, 10]
    resource_tiles = ["wheat", "wheat", "stone", "brick", "sheep", "wood", "desert"]
    
    # board = [A, B, C, D, E, F, G]
    board = {"A": {}, "B": {}, "C": {}, "D": {}, "E": {}, "F": {}, "G": {}}
    

    
    for i in board.keys():
        j = random.randint(0,len(resource_tiles) - 1)
        board[i]['resource'] = resource_tiles[j]
        del resource_tiles[j]
    
    for k in board.keys():
        if board[k]['resource'] == "desert":
            continue
        """
        Note: this is not strictly how the numbers are typically disbursed. 
        """
        m = random.randint(0,len(number_tiles) - 1)
        board[k]['number'] = number_tiles[m]
        del number_tiles[m]
    
    board["A"]["neighborhood"] = {"UR": board["B"], "R": board["C"], "LR": board["D"], "LL": board["E"], "L": board["F"], "UL": board["G"]}
    board["B"]["neighborhood"] = {"UR": None, "R": None, "LR": board["C"], "LL": board["A"], "L": board["G"], "UL": None}
    board["C"]["neighborhood"] = {"UR": None, "R": None, "LR": None, "LL": board["D"], "L": board["A"], "UL": board["B"]}
    board["D"]["neighborhood"] = {"UR": board["C"], "R": None, "LR": None, "LL": None, "L": board["E"], "UL": board["A"]}
    board["E"]["neighborhood"] = {"UR": board["A"], "R": None, "LR": None, "LL": board["D"], "L": board["A"], "UL": board["F"]}
    board["F"]["neighborhood"] = {"UR": board["G"], "R": board["A"], "LR": board["E"], "LL": None, "L": None, "UL": None}
    board["G"]["neighborhood"] = {"UR": None, "R": board["B"], "LR": board["A"], "LL": board["F"], "L": None, "UL": None}
    
    return(board)

board = create_board()
    

A_verticies = {"1": [board["A"], board["A"]["neighborhood"]['UR'], [board["A"]["neighborhood"]['R']]],
               "2": [board["A"], board["A"]["neighborhood"]['R'], [board["A"]["neighborhood"]['LR']]],
               "3": [board["A"], board["A"]["neighborhood"]['LR'], [board["A"]["neighborhood"]['LL']]],
               "4": [board["A"], board["A"]["neighborhood"]['LL'], [board["A"]["neighborhood"]['L']]],
               "5": [board["A"], board["A"]["neighborhood"]['L'], [board["A"]["neighborhood"]['UL']]],
               "6": [board["A"], board["A"]["neighborhood"]['UL'], [board["A"]["neighborhood"]['UR']]],}

"""
The board is now set. Lets create a dictionary to keep track of which resources
are abundant.
"""

def create_resource_record(board):
    resources = {"wheat": {"numbers": [], "freq": 0}, "sheep": {"numbers": [], "freq": 0}, "stone": {"numbers": [], "freq": 0},  "wood": {"numbers": [], "freq": 0},  "brick": {"numbers": [], "freq": 0},  "sevens": {"numbers": [7], "freq": 0}}
    
    for i in board.keys():
        if board[i]['resource'] == "desert":
            continue
        resources[board[i]['resource']]['numbers'].append(board[i]['number'])
    return(resources)
        
resource_record = create_resource_record(board = board)
    
"""
Lets roll the dice
"""
def roll():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return(d1 + d2)

"""
Simulate game
"""
for i in range(0, 100):
    roll_i = roll()
    print(roll_i)
    for j in resource_record.keys():
        if(roll_i in resource_record[j]['numbers']):
            resource_record[j]['freq'] = resource_record[j]['freq'] + 1



