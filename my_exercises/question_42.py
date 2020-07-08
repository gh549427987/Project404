#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 
#
# Hints:
# Use [n1:n2] notation to get a slice from a tuple.
#
################################################################

t = (1,2,3,4,5,6,7,8,9,10)
print(t[0:int(len(t)/2)])
print(t[int(len(t)/2):])