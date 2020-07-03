#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 23
# level 1
#
################################################################
#
# Question:
#     Write a method which can calculate square value of number
#
# Hints:
#     Using the ** operator
#
################################################################

def square_value(num):
    return num**2

while True:
    s = float(input("p>>"))
    if s == 'exit':
        break
    print(square_value(s))