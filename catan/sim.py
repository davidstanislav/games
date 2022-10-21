# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:34:35 2022

@author: david
"""

from catan import roll, create_board, create_resource_record, create_vertex_record

"""
Simulate game

"""

board = create_board()
resource_record = create_resource_record(board=board)
vertex_record = create_vertex_record(board=board)

print("start game")
for i in range(0, 100):
    roll_i = roll()
    print(roll_i)
    for j in resource_record.keys():
        if(roll_i in resource_record[j]['numbers']):
            resource_record[j]['freq'] = resource_record[j]['freq'] + 1
            
    for k in vertex_record.keys():
        for m in vertex_record[k].keys():
            if('number' not in vertex_record[k][m].keys()):
                continue
            
            if(vertex_record[k][m]["number"] == roll_i):
                vertex_record[k][m]["freq"] = vertex_record[k][m]["freq"] + 1