# coding: utf-8
# @Time    : 2020/7/5 1:10 下午
# @Author  : 蟹蟹 ！！
# @FileName: models.py
# @Software: PyCharm

'''
创建对象
'''

from db import db_handler

# 父类，让所有的子类继承
class Base():

    @classmethod
    def select(cls, username):
        obj = db_handler.select_data(cls, username)
        return obj

        # 保存数据 --》 注册，保存，更新数据
    def save(self):
        # 1。 获取对象的保存路径
        db_handler.save_data(self)

class admin(Base):

    def __init__(self, user, psw):
        self.user = user
        self.psw = psw
        pass

    # 创建学校
    def create_school(self, school_name, school_addr):
        ''''''
        school_obj = school(school_name, school_addr)
        school_obj.save()
        pass

    # 创建课程
    def create_course(self):
        pass

    # 创建教师
    def create_teacher(self):
        pass

class school(Base):
    def __init__(self, name, addr):
        # 必须写：self.user, 因为db_handler里面的select_data同一规范
        self.user = name
        self.addr = addr

        # 课程列表：每所学校都应该由相应的课程
        self.course_list = []


    pass

class teacher(Base):
    pass

class student(Base):
    pass

class course(Base):
    pass