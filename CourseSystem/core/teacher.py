# coding: utf-8
# @Time    : 2020/7/5 1:10 下午
# @Author  : 蟹蟹 ！！
# @FileName: teacher.py
# @Software: PyCharm

'''
教师视图
'''


def login():
    pass

def check_course():
    pass

def choose_course():
    pass

def check_student():
    pass

def update_score():
    pass

Func_dic = {
    '1':login,
    '2':check_course,
    '3':choose_course,
    '4':check_student,
    '5':update_score,
}

# 教师视图函数
def teacher_view():
    while True:
        print('''
        - 1. 登陆
        - 2. 查看教授课程
        - 3. 选择教授课程
        - 4. 查看课程下学生
        - 5. 修改学生分数
        ''')

        choice = input("请输入功能编号：").strip()

        if choice == 'q':
            break

        if choice not in Func_dic:
            print('输入有误！')
            continue


        # 通过字典调用视图函数
        Func_dic.get(choice)()