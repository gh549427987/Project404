#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
#
# Hints:
# Use if statement to judge condition.
#
################################################################

while True:
    p = input("p>>").strip()
    if p in ["Yes", 'yes', 'YES']:
        print("Yes")
    elif p == "q":
        break
    else:
        print("No")
