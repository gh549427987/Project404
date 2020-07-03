#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
#
# Hints:
# Use len() function to get the length of a string
#
################################################################

def me(a,b):
    if len(a) > len(b):
        print(a)
    elif len(a) < len(b):
        print(b)
    elif len(a) == len(b):
        print(a)
        print(b)

me('1234', '456789')
me('123121231', '32323')
me('123', '123')