#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 17
# Level 2
#
################################################################
#
# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
################################################################


deposit = 0
while True:
    transaction = input('D or W ,sir? >>>')
    money = float(transaction[1:].strip())
    if transaction[0] == 'D':
        deposit += money
        print('D {}'.format(money))
    elif transaction[0] == 'W':
        if deposit-money < 0:
            print('your poor guy!!withdraw less money please')
            continue
        deposit -= money
        print('W {}'.format(money))
    else :
        print('what you inputed got wrong!!')
        continue
    print('deposit is {}'.format(round(deposit,2)))
