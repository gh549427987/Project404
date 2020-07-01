#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 21
# Level 3
# Question£º
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2  (-1,2)
# Then, the output of the program should be:
# 2
#
################################################################
#
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
################################################################

# 初始化开始坐标
x = y = 0
position = (x,y)
while True:
    movement = input("U,D,L,R steps >>").split()
    if not movement:
        break
    movement_steps = float(movement[1])
    if movement[0] == 'U':
        y += movement_steps
    elif movement[0] == 'D':
        y -= movement_steps
    elif movement[0] == 'L':
        x -= movement_steps
    elif movement[0] == 'R':
        x += movement_steps
    else:
        print('input wrong')
        continue

    # 输出现在坐标
    print('now you are at the point {}, the distance from orginal ponit is {}'.format((round(x),round(y)), round((x**2 + y**2)**0.5)))