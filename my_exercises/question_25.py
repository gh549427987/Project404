#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 25
# Level 1
#
################################################################
#
# Question:
#     Define a class, which have a class parameter and have a same instance parameter.
#
# Hints:
#     Define a instance parameter, need add it in __init__ method
#     You can init a object with construct parameter or set the value later
#
################################################################

class person():

    def __init__(self,parameter=200, name='person', age=0):
        self.parameter = parameter
        self.name = name
        self.age = age

d = person()
d.parameter = 1000
print(d.parameter)

a = person(2000)
print(a.parameter)
b = person(30000)
print(b.parameter)
c = person(12,'cknima',30)
print(c.parameter,c.name,c.age)
e = person(32)
print(e.age)
print(e.parameter)