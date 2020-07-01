#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 13
# Level 2
#
################################################################
#
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
################################################################

inp = 'hello world! 123'
digits = 0
letters = 0
for i in inp:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1
print('LETTERS {}'.format(letters))
print('DIGHTS {}'.format(digits))