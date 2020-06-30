# coding: utf-8
# @Time    : 2020/6/24 12:44 上午
# @Author  : 蟹蟹 ！！
# @FileName: p08.py
# @Software: PyCharm

class mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        print(class_name)
        print(class_bases)
        print(class_dic)

        if not class_dic.get('__doc__'):
            raise TypeError("必须写doc，大傻叉")
        pass

    def __call__(self, *args, **kwargs):
        print("---------")
        obj = object.__new__(self)
        self.__init__(obj, *args, **kwargs)
        return obj


class Foo(object, metaclass=mymeta):
    '''
    ---------->
    '''
    def __init__(self,name):
        pass

    def walk(self):
        print('cknima')
    pass


obj = Foo # 括号调用初始化
obj(123132)
print(obj.__dict__)