# coding: utf-8
# @Time    : 2020/7/5 1:05 下午
# @Author  : 蟹蟹 ！！
# @FileName: admin.py.py
# @Software: PyCharm

'''
管理员视图
'''
from interface import admin_interface
from lib import common

admin_info = {
    'user': None,
}

def register():
    while True:
        # 输入用户名密码实现注册
        username = input('请输入用户名：').strip()
        psw = input('请输入密码：').strip()
        repsw = input('请再次输入密码：').strip()

        # 检验是否有输入,若都有进入下一步
        if username and psw and repsw:
            # 密码校验
            if psw == repsw:
                flag, msg = admin_interface.admin_register_interface(
                    username, psw
                )
                if flag:
                    print(msg)
                    # 可变类型不需要global
                    admin_info['user']= username
                    break
                else:
                    print(msg)
            else:
                print('两次密码输入不一致,清重新尝试')
                break
        else:
            print("input again")
            break

def login():
    while True:
        # 输入用户名密码实现登陆
        username = input('请输入用户名：').strip()
        psw = input('请输入密码：').strip()

        # 校验用户名和密码
        flag, msg = admin_interface.admin_login_interface(username, psw)

        if flag is True:
            admin_info['user'] = username
            print(msg)
            # 记录用户当前登陆状态

            break
        else:
            print(msg)

@common.auth('admin')
def create_school():
    while True:
        # 输入用户名密码实现登陆
        school_name = input('请输入学校名称：').strip()
        school_addr = input('请输入学校地址：').strip()

        # 校验用户名和密码
        flag, msg = admin_interface.create_school_interface(school_name, school_addr, admin_info.get('user'))

        if flag is True:
            print(msg)
            # 记录用户当前登陆状态
            break
        else:
            print(msg)

@common.auth('admin')
def create_course():
    while True:
        # 输入用户名密码实现登陆
        course_name = input('请输入课程名称：').strip()

        # 校验用户名和密码
        flag, msg = admin_interface.create_course_interface(course_name, admin_info.get('user'))

        if flag is True:
            print(msg)
            # 记录用户当前登陆状态
            break
        else:
            print(msg)

    pass

@common.auth('admin')
def create_teacher():
    pass

Func_dic = {
    '1':register,
    '2':login,
    '3':create_school,
    '4':create_course,
    '5':create_teacher,
}

# 管理员视图函数
def admin_view():
    while True:
        print("""
        - 1. 注册
        - 2. 登陆
        - 3. 创建学校
        - 4. 创建课程（先创建学校）
        - 5. 创建讲师
        """)

        choice = input("请输入功能编号：").strip()

        # 退出机制
        if choice == 'q':
            break

        # 选择选项
        if choice not in Func_dic:
            print('输入有误！')
            continue

        # 通过字典调用视图函数
        Func_dic.get(choice)()