#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
#
# Hints:
# Use % operator to check if a number is even or odd.
#
################################################################


def me(num):
    if num %2 == 0:
        print("It is an even number")
    else :
        print("It is an odd number")
me(0)
me(3)
me(4)