#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 22
# Level 3
#
################################################################
#
# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
#
# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
################################################################

def me():
    s = sorted('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'.split())
    k = sorted(set(s))
    print(sorted(k))
    dic = {}
    for i in k:
        dic[i] = 1

    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            dic['%s'%s[i]] += 1

    for i in k:
        print("{} : {}".format(i, dic[i]))

def you():
    freq = {}
    s = sorted('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'.split())
    for word in s:
        freq['%s'%word] = freq.get(word, 0 )+1
    words = freq.keys()
    sorted(words)
    for i in words:
        print('%s : %d'%(i,freq['%s'%i]))

you()