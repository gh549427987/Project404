# coding: utf-8
# @Time    : 2020/6/22 10:19 下午
# @Author  : 蟹蟹 ！！
# @FileName: p01.py
# @Software: PyCharm


# 之前文件内指针的移动都是由读/写操作而被动触发的，若想读取文件某一特定位置的数据，则则需要用f.seek方法主动控制文件内指针的移动，详细用法如下：
# f.seek(指针移动的字节数,模式控制):
# 模式控制:
# 0: 默认的模式,该模式代表指针移动的字节数是以文件开头为参照的
# 1: 该模式代表指针移动的字节数是以当前所在的位置为参照的
# 2: 该模式代表指针移动的字节数是以文件末尾的位置为参照的
# 强调:其中0模式可以在t或者b模式使用,而1跟2模式只能在b模式下用
def btmode():
    # t模式的使用
    with open('test.txt', 'rt', encoding='utf-8') as f:
        res = f.read()
        print(type(res))

    with open('test.txt', 'wt', encoding='utf-8') as f:
        res = f.write('爱你一辈子')
        f.write('')

    # b模式的使用
    with open('原来是萝卜丫 - 是心动啊 (翻自 iu／High4).flac', 'rb') as f:
        data = f.read()
        print(type(data))

    with open('原来是萝卜丫 - 是心动啊 (翻自 iu／High4).flac', 'wb') as f:
        msg = "你好"
        res = msg.encode('utf-8')
        f.write(res)

def copytool():
    src_file = input('原文件路径: ').strip()
    dst_file = input('目标文件路径: ').strip()
    with open(r'%s' %src_file, mode='rb') as read_f,open(r'%s' %dst_file, mode='wb') as write_f:
        for line in read_f:
            write_f.write(line)

def mode0():
    with open('test.txt','rt',encoding='utf-8') as f:
        f.seek(3,0)
        print(f.tell())
        print(f.read())

    with open('test.txt', 'rb') as f:
        f.seek(3,0)
        print(f.read().decode('utf-8'))

def mode1():
    with open('test.txt', 'rb') as f:
        f.seek(3,1)
        print(f.tell())
        f.seek(3,1)
        print(f.tell())
        print(f.read().decode('utf-8'))

        text = u'爱'
        print(text)

def mode2():
    with open('test.txt', 'rb') as f:
        f.seek(0,2)
        print(f.tell())
        f.seek(-3,2)
        print(f.read().decode('utf-8'))

    import time
    with open('test.log', 'rb') as f:
        f.seek(0,2)
        while True:
            line = f.readline()
            if len(line) == 0:
                time.sleep(0.5)
            else:
                print(line.decode('utf-8'), end="")


def foo(x, y, *args):
    print(x)
    print(y)
    print(args)


# 可变长度的位置参数
def add(*args):
    res = 0
    for i in args:
        res += i
    return res


# 可变长度的关键字参数
def foo2(x, **kwargs):
    return kwargs

def register(name, age, *, sex, height):
    pass
# 提示： *args、**kwargs中的args和kwargs被替换成其他名字并无语法错误，但使用args、kwargs是约定俗成的。


import time
def index(num):
    time.sleep(num)
    print('welcome')
    return 200

def wrapper(func): # 通过参数接收外部的值
    start_time=time.time()
    res=func()
    stop_time=time.time()
    print('run time is %s' %(stop_time-start_time))
    return res

# 这便违反了不能修改被装饰对象调用方式的原则，于是我们换一种为函数体传值的方式，即将值包给函数，如下
def timer(func):
    def wrapper(*args,**kwargs): # 通过参数接收外部的值
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
        return res
    return wrapper


def timer2(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('run time2 is %s' %(stop_time-start_time))
        return res
    return wrapper

# index = timer(timer2(index))
# index(2)
# 多重装饰可以这么理解，timer2返回wrapper方法，wrapper方法返回index的方法，所以timer2返回的是index的方法


__N = 0