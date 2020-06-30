# coding: utf-8
# @Time    : 2020/6/23 11:28 下午
# @Author  : 蟹蟹 ！！
# @FileName: p07_2.py
# @Software: PyCharm

class mymeta(type):

    def __new__(cls, name, bases, attrs):
        update_attrs={}

        for k,v in attrs.items():
            if callable(v):
                print("%s and %s are callable"%(k,v))


        for k,v in attrs.items():
            # not callable 判断不是函数（function）
            # not startswith 判断不是系统定义名字，类中私有变量等等
            if not k.startswith('__') and not callable(v):
                update_attrs[k.upper()]=v
            else:
                update_attrs[k] = v
        return type.__new__(cls, name, bases, update_attrs)
    pass

class peopel(metaclass=mymeta):

    country = "China"
    tag = 'LOL'

    def walk(self):
        print(self.name)

print(peopel.__dict__)