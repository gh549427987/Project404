# coding: utf-8
# @Time    : 2020/7/13 10:32 下午
# @Author  : 蟹蟹 ！！
# @FileName: start.py
# @Software: PyCharm

import a24_changeENV as a24

version = {
    '1':a24.toOnline,
    '2':a24.toTest,
    '3':a24.toDefalut,
    '4':a24.currentVersion,
    '5':a24.saveReg
}



while True:
    # 1）用户视图，选择需要切换的环境；
    envChoose = input('Welcome man,this script is work for change register.\n'
                      '1: Change to Online Env.\n'
                      '2: Change to Test Env.\n'
                      '3: Change to Default Env.\n'
                      '4: 查询当前是什么环境.\n'
                      '5: 保存当前环境的注册表.\n'
                      'q: quit.\n'
                      'choose a selection you want>> ').strip()
    if envChoose in ['1','2','3']:
        version[envChoose]()
        break
    elif envChoose in ['4','5']:
        version[envChoose]()
        continue
    elif envChoose == 'q':
        break
    else:
        print('功能编号选择错误!')
        continue