# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 12:02:24 2018

@author: USER
"""

dict = {'fname' : 'Shashwat',
        'lname' : 'Singh',
        'age' : 32}

dict['fname'] = "Hello"

def add(a,b):
    return a+b

add(3,4)

def f(x):
    return x % 3 == 0 or x % 5 == 0

list = filter(f, range(1,30))


def cube(x):
    return x*x*x

list = map(cube, range(2,25))


def add(x,y):
    return x+y

reduce(add, range(2,4))