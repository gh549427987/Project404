# coding: utf-8
# @Time    : 2020/7/5 1:10 下午
# @Author  : 蟹蟹 ！！
# @FileName: admin_interface.py
# @Software: PyCharm

from db import models

# 管理员注册接口
def admin_register_interface(username, password):

    # 1. user exist or nont
    # 调用admin类中， select,由该方法去调用db_handler中的selcet_data功能获取对象
    admin_obj = models.admin.select(username)

    # 1.1)若存在， 不允许注册，返回用户给视图层
    if admin_obj:
        return False,'用户已存在'

    # 1.2)若不存在，则允许注册，调用类实例化得到对象并保存
    asmin_obj = models.admin(username, password)
    # 对象调用save()
    asmin_obj.save()
    return True, '注册成功'
    pass

def admin_login_interface(username, psw):
    # 1. 判断用户是否存在
    admin_obj = models.admin.select(username)

    # 2. 若用户不存在，返回False
    if not admin_obj:
        return False, '用户不存在'

    # 3）若用户存在，则校验密码
    if psw == admin_obj.psw:
        return True, '登陆成功'
    else:
        return False, '密码错误'

def create_school_interface(school_name, school_addr, admin_name):
    # 1. 查看学校是否已存在
    # school_obj 有可能是对象或者是None
    school_obj = models.school.select(school_name)
    # 2.若学校存在则返回false，告诉用户已存在
    if school_obj:
        return False, '学校已经存在'

    # 3。若不存在，则创建学校，告诉用户已创建（由管理员对象来创建）
    admin_obj = models.admin.select(admin_name)
    # 由管理员来调用创建学校方法，并传入学校的名字与地址
    admin_obj.create_school(
        school_name, school_addr
    )
    # 返回创建学校成功给视图层
    return True, f'[{school_name}]学校创建成功!'

