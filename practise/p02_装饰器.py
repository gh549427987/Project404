# coding: utf-8
# @Time    : 2020/6/22 10:19 下午
# @Author  : 蟹蟹 ！！
# @FileName: p01.py
# @Software: PyCharm

__all__ = ['auth']
from functools import wraps
def auth(driver):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            with open(driver, 'rb') as f:
                r = f.read().decode('utf-8')
                print(r)
            return res

        return wrapper

    return deco

@auth(driver='test.txt')
def index():
    '''
    Nothing
    wock
    :return:
    '''
    pass

print(help(index))