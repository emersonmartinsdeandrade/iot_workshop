# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 11:55:35 2018

@author: USER
"""

count = 0
list = [1,4,2,5,1,4,4,2]

for i in list:
    if i == 4:
        count += 1

for i in range(0, count):
    list.remove(4)