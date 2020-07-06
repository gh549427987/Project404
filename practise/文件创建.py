# coding: utf-8
# @Time    : 2020/7/4 1:03 上午
# @Author  : 蟹蟹 ！！
# @FileName: 文件创建.py
# @Software: PyCharm
import os
old_filename = 'test.txt'
new_filename = 'test.txt.new'
f = open(old_filename,'r')
f_new = open(new_filename,'w')

old_str = 'account'
new_str = 'new_account'

for line in f:
    if 'account' in line:
        line = line.replace(old_str, new_str)
    f_new.write(line)

f.close()
f_new.close()
os.rename(new_filename, old_filename)
