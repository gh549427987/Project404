# coding: utf-8
# @Time    : 2020/7/5 1:09 下午
# @Author  : 蟹蟹 ！！
# @FileName: src.py
# @Software: PyCharm

'''
用户视图层 主视图
'''


from core import admin
from core import teacher
from core import student
Func_dic = {
    '1':admin.admin_view,
    '2':teacher.teacher_view,
    '3':student.student_view,
}

def run():
    while True:
        print('''
        ================ 欢迎来到选课系统 ================
        1. 管理员功能
        2. 学生功能
        3. 教师功能
        ================      end       ================
        ''')

        choice = input("请输入功能编号：").strip()

        # 退出机制
        if choice == 'q':
            break

        # 读取选择
        if choice not in Func_dic:
            print('输入有误！')
            continue

        # 通过字典调用视图函数
        Func_dic.get(choice)()
