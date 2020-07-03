#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
#
# Hints:
# Use int() to convert a string to integer.
#
################################################################

def me():
    s = input("P>>").split()
    sum = 0
    for i in s:
        sum += int(i)
    print(sum)

me()
00

