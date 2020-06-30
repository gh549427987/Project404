# coding: utf-8
# @Time    : 2020/6/23 4:02 下午
# @Author  : 蟹蟹 ！！
# @FileName: p02_迭代器.py
# @Software: PyCharm

goods=['mac','lenovo','acer','dell','sony']

index=0
while index < len(goods):
    print(goods[index])
    index+=1

i = iter(goods)
while True:
    try:
        print(next(i))
    except StopIteration:
        pass
