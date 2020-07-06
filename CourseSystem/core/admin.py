# coding: utf-8
# @Time    : 2020/7/5 1:05 下午
# @Author  : 蟹蟹 ！！
# @FileName: admin.py.py
# @Software: PyCharm

'''
管理员视图
'''

def register():
    while True:
        # 输入用户名密码实现注册
        username = input('请输入用户名：').strip()
        psw = input('请输入密码：').strip()
        repsw = input('请再次输入密码：').strip()

        # 检验是否有输入,若都有进入下一步
        if username and psw and repsw:
            # 密码校验
            if psw != repsw:
                print('注册失败，两次密码输入不一致！')
                continue

            # 用户名校验，待完善
            if not username:
                pass
    pass

def login():
    while True:
        # 输入用户名密码实现登陆
        username = input('请输入用户名：').strip()
        psw = input('请输入密码：').strip()

        # 校验用户名和密码
        pass

    pass

def create_school():
    pass

def create_course():
    pass

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