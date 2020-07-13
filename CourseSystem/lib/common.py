# coding: utf-8
# @Time    : 2020/7/5 1:12 下午
# @Author  : 蟹蟹 ！！
# @FileName: common.py
# @Software: PyCharm

''''
公共方法
'''

def auth(role):
    '''
    :param role: 角色，管理员/学生/老师
    :return:
    '''
    from core import admin, student, teacher
    def login_auth(func):
        def inner(*args, **kwargs):
            if role == 'admin':
                if admin.admin_info['user']:
                   res = func(*args, **kwargs)
                   return res
                else:
                    print('请先登录管理员账号')
                    admin.login()

            elif role == 'student':
                if student.student_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('请先登陆学生账号')
                    student.login()

            elif role == 'teacher':
                if teacher.teacher_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('请先登陆教师账号')
                    teacher.login()
            else:
                print("当前视图没有权限")
        return inner
    return login_auth