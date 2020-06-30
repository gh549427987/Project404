# coding: utf-8
# @Time    : 2020/6/23 4:27 下午
# @Author  : 蟹蟹 ！！
# @FileName: p03_生成器.py
# @Software: PyCharm

def myrange(start, stop, step=1):
    print('start......')
    while start<stop:
        yield start
        start+=step
    print('end......')

# g = myrange(0,3)
# for i in g:
#     # print(i)
#     pass
# 针对表达式形式的yield，生成器对象必须事先被初始化一次，让函数挂起在food=yield的位置，等待调用g.send()方法为函数体传值，g.send(None)等同于next(g)。

from functools import wraps
def init(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return wrapper

@init
def eater():
    print('Ready to eat ')
    while True:
        food = yield
        print('get the food: %s, and start to eat' %food)


@init
def eater2():
    print("Ready to eat")
    food_list = []
    while True:
        food = yield food_list
        food_list.append(food)
        print(food_list)

g = eater2()
g.send('包子')
g.send('饺子')

# 如果我们要读取一个大文件的字节数，应该基于生成器表达式的方式完成
with open('db.txt','rb') as f:
    nums=(len(line) for line in f)
    total_size=sum(nums) # 依次执行next(nums)，然后累加到一起得到结果=