# coding: utf-8
# @Time    : 2020/6/27 11:19 上午
# @Author  : 蟹蟹 ！！
# @FileName: p09.py.py
# @Software: PyCharm

name = input('input your name >> ')
psw = input('input your psw >> ')
with open('test.txt', 'at') as f:
    f.write("your account is: %s \n"
            "your pasw is: %s \n")
