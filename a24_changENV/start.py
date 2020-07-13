# coding: utf-8
# @Time    : 2020/7/13 10:32 下午
# @Author  : 蟹蟹 ！！
# @FileName: start.py
# @Software: PyCharm

import a24_changeENV as a24


version = {
    '1':a24.toOnline,
    '2':a24.toTest,
}

# 1）用户视图，选择需要切换的环境；
envChoose = input('Welcome man,this script is work for change register.\n'
                        '1: Change to Online Env.\n'
                        '2: Change to Test Env.\n'
                        'q: quit.\n'
                        'choose a selection you want>> ').strip()

while True:
    if envChoose in version.keys():
        version[envChoose]()
        break
    elif envChoose == 'q':
        break
    else:
        continue