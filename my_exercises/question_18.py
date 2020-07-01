#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 18
# Level 3
#
################################################################
#
# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
################################################################

print('welcome to register!')
# username = input('please input your username')
# password = input('please input your password')

password = 'ABd1234@1,a F1#,2w3E*,2We3345,       d123D#d'.split(',')

def mymethod():
    # set() including 'digit','lower','upper','special' means success
    typeChaSet = set()
    for psw in password:
        typeChaSet.clear()
        if not len(psw) <= 12 and len(psw) >= 6:
            print('{}\'s lenght is wrong!'.format(psw))
            continue
        for i in psw:
            if i.isdigit():
                typeChaSet.add('digit')
                continue
            elif i.islower():
                typeChaSet.add('lower')
                continue
            elif i.isupper():
                typeChaSet.add('upper')
                continue
            elif i in '$#@':
                typeChaSet.add('special')
                continue
            else:
                break
        if len(typeChaSet) == 4:
            print('{} is passed'.format(psw))
            print(typeChaSet)
        else:
            print('{} is not passed'.format(psw))
            print(typeChaSet)

import re
def method():
    value = []
    for psw in password:
        if 6<=len(psw)<=12:
            pass
        else:
            continue
        if not re.search("[0-9]", psw):
            continue
        elif not re.search("[a-z]", psw):
            continue
        elif not re.search("[A-Z]", psw):
            continue
        elif not re.search("[$@#]", psw):
            continue
        elif re.search("\s", psw):
            continue
        else:
            value.append(psw)
            pass
    return value
print(method())
print("cknima \s")


# for i in password:
#     correct_digit = True
#     correct_alpha_upper = True
#     correct_specialCha = True
#     correct_alpha_lower = True
#     for j in i:
#         correct_digit = True
#         correct_alpha_upper = True
#         correct_specialCha = True
#         correct_alpha_lower = True
#         if not i.isdigit() :
#             correct_digit = False
#         if not i.isupper():
#             correct_alpha_upper = False
#         if not i.lower():
#             correct_alpha_lower = False
#         if not i in ['$#@']:
#             correct_specialCha = False
# 
#         if correct_digit == True or correct_alpha_upper == True or correct_alpha_lower == True or correct_specialCha \
#                 == \
#             True:
#             correct = True
#             continue
#         else:
#             correct = False
#             print('your pass is Wrong')
#             continue
#     if correct_digit == True and correct_alpha_upper == True and correct_alpha_lower == True and correct_specialCha \
#             == \
#             True:
#         correct = True
#         print('{} is correct'.format(i))
#         continue




# print('=======================')
# if '弟'.islower():
#     print(True)
# else:
#     print(False)