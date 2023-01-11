# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 15:31:18 2023

@author: djstanis
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 100)
y = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y, color='green')
# ax.plot(y, x, color='green')

fig.show()
fig.savefig('figure.pdf')


fig1, ax1 = plt.subplots()
ax1.plot(x, y, color='red')
fig1.show()

fig2, ax2 = plt.subplots()
ax2.bar(["david", "alex", "charlie"], [10, 5, 20], color='black')
fig2.show()
