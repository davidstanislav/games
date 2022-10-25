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

    board = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G}
    
    
    board["A"]["neighborhood"] = {"UR": "B", "R": "C", "LR": "D", 
                              "LL": "E", "L": "F", "UL": "G"}
    board["B"]["neighborhood"] = {"UR": None, "R": None, "LR": "C", 
                                  "LL": "A", "L": "G", "UL": None}
    board["C"]["neighborhood"] = {"UR": None, "R": None, "LR": None, 
                                  "LL": "D", "L": "A", "UL": "B"}
    board["D"]["neighborhood"] = {"UR": "C", "R": None, "LR": None, 
                                  "LL": None, "L": "E", "UL": "A"}
    board["E"]["neighborhood"] = {"UR": "A", "R": "D", "LR": None, 
                                  "LL": None, "L": None, "UL": "F"}
    board["F"]["neighborhood"] = {"UR": "G", "R": "A", "LR": "E", 
                                  "LL": None, "L": None, "UL": None}
    board["G"]["neighborhood"] = {"UR": None, "R": "B", "LR": "A", 
                                  "LL": "F", "L": None, "UL": None}
    
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

    for i in board.keys():
        verticies = {"1": [i, board[i]["neighborhood"]['UR'], board[i]["neighborhood"]['R']],
                        "2": [i, board[i]["neighborhood"]['R'], board[i]["neighborhood"]['LR']],
                        "3": [i, board[i]["neighborhood"]['LR'], board[i]["neighborhood"]['LL']],
                        "4": [i, board[i]["neighborhood"]['LL'], board[i]["neighborhood"]['L']],
                        "5": [i, board[i]["neighborhood"]['L'], board[i]["neighborhood"]['UL']],
                        "6": [i, board[i]["neighborhood"]['UL'], board[i]["neighborhood"]['UR']]                  
                        }
        board[i]['verticies'] = verticies    

    return(board)


def create_resource_record(board):
    """
    The board is now set. Lets create a dictionary to keep track of which resources
    are abundant.
    """
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

    
def create_vertex_record(board):
    """
    This will create a dictionary of every vertex. Each vertex object will have an attribute 'numbers'
    to indicate 
    """
    vert_record = {}
    for i in board.keys():
        for j in board[i]['verticies'].keys():
            vert_key_ij = str(i) + str(j)
            vert_record[vert_key_ij] =  {"wheat": {"freq": 0}, 
                                         "sheep": {"freq": 0}, 
                                         "stone": {"freq": 0},  
                                         "wood": {"freq": 0},  
                                         "brick": {"freq": 0},
                                         "desert": {"freq": 0}}
            print(vert_key_ij)
            neighbors = board[i]['verticies'][j]
            neighbors = [m for m in neighbors if m is not None]
            for k in neighbors:
                resource = board[k]['resource']
                number = board[k]['number']
                print(resource + " " + str(number))
                vert_record[vert_key_ij][resource]["number"] = number
    
    
    return(vert_record)


def roll():
    """
    Lets roll the dice
    """
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return(d1 + d2)

def roll_alt(num_sides):
    
    d1 = random.randint(1,num_sides)
    
    return(d1)



f100 = roll_alt(num_sides=100)

f12 = roll_alt(num_sides=12)


if __name__ == "__main__":
    board = create_board()
    vertex_record = create_vertex_record(board=board)


