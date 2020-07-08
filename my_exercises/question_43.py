#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
#
# Hints:
# Use "for" to iterate the tuple
# Use tuple() to generate a tuple from a list.
#
################################################################

def me():
    list = []
    for i in (1,2,3,4,5,6,7,8,9,10):
        if i%2 == 0:
            list.append(i)
    return tuple(list)
print(me())