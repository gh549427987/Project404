# coding: utf-8
# @Time    : 2020/6/23 9:08 下午
# @Author  : 蟹蟹 ！！
# @FileName: p07_1.py
# @Software: PyCharm

class mymeta(type):

    def __call__(self, *args, **kwargs):
        obj = self.__new__(self)
        self.__init__(obj, *args, **kwargs)
        return obj

class people(object, metaclass=mymeta):
    school = 'standford'

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
        print('%s says welcome to the Stanford to learn Python' %self.name)

t1=people('lili',18)
print(t1.__dict__) #{'name': 'lili', 'age': 18}