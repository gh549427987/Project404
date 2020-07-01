#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 20
# Level 3
#
################################################################
#
# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
#
# Hints:
# Consider use yield
#
################################################################

class me():

    def __init__(self):
        pass

    def gener(self, num):
        for i in range(0, num):
            if i%7 == 0:
                yield i

d = me()
print()

def you(n):
    for i in range(0,n):
        if i%7==0:
            yield i

generator = you(2000)
g2 = d.gener(2000)
while True:
    s = input("p>>")
    if not s != 'exit':
        break
    print(next(g2))