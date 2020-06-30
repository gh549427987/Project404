# coding: utf-8
# @Time    : 2020/6/24 12:03 上午
# @Author  : 蟹蟹 ！！
# @FileName: p07_4.py
# @Software: PyCharm

class mymeta(type):

    def __new__(cls, name, bases, attrs):
        update_attrs = {}
        obj = cls.__new__(name, bases, attrs)
        print(attrs.items())
    pass

class Chinese(metaclass=mymeta):

    country='China'
    tag='Legend of the Dragon' #龙的传人
    def walk(self):
        print('%s is walking' %self.name)
    pass

p = Chinese()
print(p.__dict__)