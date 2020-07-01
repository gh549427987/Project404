#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 15
# Level 2
#
################################################################
#
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
############################0####################################

a = int(input('P>>'))
aa = 10*a+a
aaa = 100*a + 10*a + a
aaaa = 1000*a + 100*a + 10*a +a
print('{}'.format(a+aa+aaa+aaaa))

