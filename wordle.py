# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:09:02 2022

@author: djstanis
"""

import wordfreq as wf
import pandas as pd
from datetime import date

def previous_wordles():
    words = {'word': ['point', 'robot', 'prick', 'wince', 'crimp', 
                      'knoll', 'sugar', 'whack', 'mount', 'perky', 
                      'could', 'wrung', 'light', 'those', 'moist'],
             'date': [date(2022, 1, 18), date(2022, 1, 19), date(2022, 1, 21),
                      date(2022, 1, 22), date(2022, 1, 23), date(2022, 1, 24), 
                      date(2022, 1, 25), date(2022, 1, 26), date(2022, 1, 27), 
                      date(2022, 1, 28), date(2022, 1, 29), date(2022, 1, 30), 
                      date(2022, 1, 31), date(2022, 1, 2), date(2022, 2, 2)]}
    df = pd.DataFrame(data=words)
    freq = []
    for i in words['word']:
        x = wf.word_frequency(i, 'en')
        freq.append(x)
    df['freq'] = freq
    return(df)


def todays_wordle(word):
    x = {'date': date.today(),
           'word': word,
           'freq': wf.word_frequency(word, 'en')
           }
    return(x)