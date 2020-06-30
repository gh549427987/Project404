# coding: utf-8
# @Time    : 2020/6/23 11:52 下午
# @Author  : 蟹蟹 ！！
# @FileName: p07_3.py
# @Software: PyCharm

class mymeta(type):

    def __call__(self, *args, **kwargs):
        if args:
            raise (TypeError('must use keyword argument'))

        obj = self.__new__(self)

        for k,v in kwargs.items():
            obj.__dict__[k.upper()]=v
        return obj

    pass

class Chinese(metaclass=mymeta):
    country='China'
    tag='Legend of the Dragon' #龙的传人
    def walk(self):
        print('%s is walking' %self.name)
    pass

p = Chinese(name='lili')
print(p.__dict__)