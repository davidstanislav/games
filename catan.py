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
    
    
    A = {}
    B = {}
    C = {}
    D = {}
    E = {}
    F = {}
    G = {}
    # board = [A, B, C, D, E, F, G]
    board = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G}
    
    board["A"]["neighborhood"] = {"UR": B, "R": C, "LR": D, 
                                  "LL": E, "L": F, "UL": G}
    
    board["B"]["neighborhood"] = {"UR": None, "R": None, "LR": C, "LL": A, "L": G, "UL": None}
    board["C"]["neighborhood"] = {"UR": None, "R": None, "LR": None, "LL": D, "L": A, "UL": B}
    board["D"]["neighborhood"] = {"UR": C, "R": None, "LR": None, "LL": None, "L": E, "UL": A}
    board["E"]["neighborhood"] = {"UR": A, "R": None, "LR": None, "LL": D, "L": A, "UL": F}
    board["F"]["neighborhood"] = {"UR": G, "R": A, "LR": E, "LL": None, "L": None, "UL": None}
    board["G"]["neighborhood"] = {"UR": None, "R": B, "LR": A, "LL": F, "L": None, "UL": None}
    
    for i in board.keys():
        j = random.randint(0,len(resource_tiles) - 1)
        board[i]['resource'] = resource_tiles[j]
        del resource_tiles[j]
    
    for k in board.keys():
        if board[k]['resource'] == "desert":
            board[k]['number'] = 0
            continue
        """
        Note: this is not strictly how the numbers are typically disbursed. 
        """
        m = random.randint(0,len(number_tiles) - 1)
        board[k]['number'] = number_tiles[m]
        del number_tiles[m]
    # return(board)

    
    return(board)

board = create_board()

for i in board.keys():
    verticies = {"1": [board[i], board[i]["neighborhood"]['UR'], board[i]["neighborhood"]['R']],
                   "2": [board[i], board[i]["neighborhood"]['R'], board[i]["neighborhood"]['LR']],
                   "3": [board[i], board[i]["neighborhood"]['LR'], board[i]["neighborhood"]['LL']],
                   "4": [board[i], board[i]["neighborhood"]['LL'], board[i]["neighborhood"]['L']],
                   "5": [board[i], board[i]["neighborhood"]['L'], board[i]["neighborhood"]['UL']],
                   "6": [board[i], board[i]["neighborhood"]['UL'], board[i]["neighborhood"]['UR']]                  
                   }
    board[i]['verticies'] = verticies

"""
The board is now set. Lets create a dictionary to keep track of which resources
are abundant.
"""

def create_resource_record(board):
    resources = {"wheat": {"numbers": [], "freq": 0}, 
                 "sheep": {"numbers": [], "freq": 0}, 
                 "stone": {"numbers": [], "freq": 0},  
                 "wood": {"numbers": [], "freq": 0},  
                 "brick": {"numbers": [], "freq": 0},  
                 "sevens": {"numbers": [7], "freq": 0}}
    
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



