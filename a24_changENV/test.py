# coding: utf-8
# @Time    : 2020/7/8 11:45 下午
# @Author  : 蟹蟹 ！！
# @FileName: test..py
# @Software: PyCharm

from conf import conf
import time
import os
oldtype = 'Online'
_regJson = '{}/{}_env/{}_latest.json'.format(conf.REG_PATH,oldtype,oldtype)
curr_time = time.strftime("%Y-%m-%d_%H:%M:%S")
_regBackup = '{}/{}_env/{}_{}.json'.format(oldtype, oldtype, oldtype, curr_time)

os.popen('copy {} {}'.format(_regJson.replace('\\','\\\\'),_regBackup.replace('\\','\\\\')))
print('copy {} {}'.format(_regJson.replace('\\','\\\\'),_regBackup.replace('\\','\\\\')))