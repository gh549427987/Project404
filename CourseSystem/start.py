# coding: utf-8
# @Time    : 2020/7/5 1:13 下午
# @Author  : 蟹蟹 ！！
# @FileName: start.py
# @Software: PyCharm

# 启动环境-虚拟环境
# /Users/jhua/PycharmProjects/Project404/CourseSystem/env_CourseSystem/bin/python /Users/jhua/PycharmProjects/Project404/CourseSystem/start.py
# __file__ 当前文件的绝对地址 ：/Users/jhua/PycharmProjects/Project404/CourseSystem/start.py
import os, sys

sys.path.append(
    os.path.dirname(__file__)
)

from core import src
if __name__ == '__main__':
    src.run()