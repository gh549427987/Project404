#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 5
# Level 1
#
################################################################
#
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters
#
################################################################

class al():

    def __init__(self):
        s = ''
        pass

    def getString(self):
        self.s = input('p>>')
        return self.s
        pass

    def printString(self):
        print(self.s.upper())
        pass

a = al()
a.getString()
a.printString()