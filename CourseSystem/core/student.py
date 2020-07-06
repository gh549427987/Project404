# coding: utf-8
# @Time    : 2020/7/5 1:09 下午
# @Author  : 蟹蟹 ！！
# @FileName: student.py
# @Software: PyCharm
'''
学生视图
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
    pass

def choose_school():
    pass

def choose_course():
    pass

def check_score():
    pass

Func_dic = {
    '1':register,
    '2':login,
    '3':choose_school,
    '4':choose_course,
    '5':check_score,
}

# 学生视图函数
def student_view():
    while True:
        print('''
        - 1. 注册
        - 2. 登陆
        - 3. 选择学校
        - 4. 选择课程（先选择学校，再选择课程）
        - 5. 查看分数
        ''')


        choice = input("请输入功能编号：").strip()


        if choice == 'q':
            break

        if choice not in Func_dic:
            print('输入有误！')
            continue



        # 通过字典调用视图函数
        Func_dic.get(choice)()