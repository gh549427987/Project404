# coding: utf-8
# @Time    : 2020/6/23 3:04 下午
# @Author  : 蟹蟹 ！！
# @FileName: compare01.py
# @Software: PyCharm
import time


def index(num):
    time.sleep(num)
    print('welcome')
    return 200


def timer(func):
    def wrapper(*args,**kwargs): # 通过参数接收外部的值
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
        return res
    return wrapper

index = timer(index)
index(2)