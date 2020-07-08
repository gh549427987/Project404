#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
#
# Hints:
# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.
#
################################################################

list = [1,2,3,4,5,6,7,8,9,10]
s = filter(lambda x:x%2==0 , list)
while True:
    p = input("p>>")
    print(next(s))
