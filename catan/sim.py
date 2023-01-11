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
                
                
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

resources = resource_record.keys()

fig2, ax2 = plt.subplots()
freqs = [resource_record['wheat']['freq'], resource_record['sheep']['freq'], resource_record['stone']['freq'],resource_record['wood']['freq'],resource_record['brick']['freq'], resource_record['sevens']['freq']]
ax2.bar(resources, freqs, color=['gold', 'lightgreen', 'darkgrey', 'darkolivegreen', 'darkred', 'black'])
fig2.show()