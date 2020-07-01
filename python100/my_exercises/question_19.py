''#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 19
# Level 3
#
################################################################
#
# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use itemgetter to enable multiple sort keys.
#
################################################################

def me():
    list = "Tom,19,80;Tom,23,70;John,20,90;Jony,17,91;Jony,17,93;Jony,18,100;Json,21," \
           "85".split(';')
    givenData = [tuple(data.split(',')) for data in list]

    sortFirst = sorted(givenData) # name rank
    print("the Fisrt sort \n{}".format(sortFirst))

    # 先确认一遍重名的givenData
    sameSet = set()
    begin = False
    for i in range(len(sortFirst)-1):
        if not sortFirst[i][0] == sortFirst[i+1][0]: # 如果name相同的话，记下来
            if begin is True:
                # age rank
                # 年龄越大，越靠前
                maxindex = max(sameSet)
                minindex = min(sameSet)
                maxage = tuple()
                for j in range(minindex, maxindex+1):
                    for k in range(j, maxindex-1):
                        if int(sortFirst[j]) >= int(sortFirst[k+1]):
                            maxage = sortFirst[j]
                        else:
                            maxage = sortFirst[k+1]
                    sortFirst[j] = maxage # 将一轮比较下最大的值提取出来，作为maxage保存到j位置上

            sameSet.clear()
            begin = False
            continue
        else:
            begin = True
            sameSet.add(i)
            sameSet.add(i+1)

        print(sameSet)

def you():
    from operator import itemgetter, attrgetter
    l = []
    while True:
        s = input("p>>")
        if not s:
            break
        l.append(tuple(s.split(',')))
    print(sorted(l, key=itemgetter(0,1,2)))
you()