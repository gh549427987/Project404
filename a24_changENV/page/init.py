# coding: utf-8
# @Time    : 2020/7/21 10:19
# @Author  : 蟹蟹 ！！
# @FileName: init.py.py
# @Software: PyCharm

from common import a24_init as ai

init_dic = {
    '1': ai.installOnline,  # 安装正式环境
    '2': ai.creatDir,  # 创建所有目录
}

def init():
    while True:
        # 1）初始化视图；
        p = input('Welcome man,this script is work for change register.\n'
                          '1: 安装正式环境.\n'
                          '2: 安装测试环境.\n'
                          '3: 创建指定目录.\n'
                          'q: quit.\n'
                          'choose a selection you want>> ').strip()

        if p in init_dic.keys():
            init_dic[p]()


