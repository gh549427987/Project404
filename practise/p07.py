# coding: utf-8
# @Time    : 2020/6/23 8:50 下午
# @Author  : 蟹蟹 ！！
# @FileName: p07.py
# @Software: PyCharm

class mymeta(type):

    def __init__(self, class_name, class_bases, class_dic):
        super().__init__(class_name, class_bases, class_dic)

        if class_name.islower():
            raise  TypeError('类名%s请修改为驼峰体' %class_name)

        if '__doc__' not in class_dic or len(class_dic['__doc__'].strip('\n'))==0:
            raise TypeError('类中必须有文档注释，并且文档注释不能为空')

    def __call__(self, *args, **kwargs):
        print(*args)
        print(**kwargs)

class superMan(object, metaclass=mymeta):
    '''
    cknima
    '''
    def  __init__(self):
        pass



superMan('lili', 18)