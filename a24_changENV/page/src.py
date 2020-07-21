# coding: utf-8
# @Time    : 2020/7/14 20:30
# @Author  : 蟹蟹 ！！
# @FileName: src.py
# @Software: PyCharm

from common import a24_changeENV as a24
from conf import conf
from page import init
import logging

version = {
    '1':a24.toOnline,
    '2':a24.toTest,
    '3':a24.toDefault,
    '4':a24.currentVersion,
    '5':a24.saveReg,
    '6':a24.setReg,
    '7':init.init,
}

def run():
    while True:
        # 1）用户视图，选择需要切换的环境；
        envChoose = input('Welcome man,this script is work for change register.\n'
                          '1: Start Online Env.\n'
                          '2: Start Test Env.\n'
                          '3: Start Default Env.\n'
                          '4: 查询当前是什么环境.\n' 
                          '5: 保存当前环境的注册表.\n'
                          '6: 注入当前版本的注册表.\n'
                          '7: 初始化环境.\n'
                          'q: quit.\n'
                          'choose a selection you want>> ').strip()
        if envChoose in version.keys():
            version[envChoose]()
            continue
        elif envChoose == 'q':
            break
        else:
            print('功能编号选择错误!')
            continue