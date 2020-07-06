# coding: utf-8
# @Time    : 2020/7/4 2:04 上午
# @Author  : 蟹蟹 ！！
# @FileName: 股票查询.py
# @Software: PyCharm

with open('stock_data.txt', 'r') as f:
    title = f.readline().split()
    print(title)