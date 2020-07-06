#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 16
# Level 2
#
################################################################
#
# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
################################################################

d = '1,2,3,4,5,6,7,8,9'.split(',')
oddNumeber = []
for i in d:
    if int(i)%2 != 0:
        oddNumeber.append(i)

oddNumeber2 = [x for x in d if int(x)%2 != 0]
print(','.join(oddNumeber2))

print(oddNumeber)