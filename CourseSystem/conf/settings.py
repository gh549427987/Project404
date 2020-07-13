# coding: utf-8
# @Time    : 2020/7/5 1:11 下午
# @Author  : 蟹蟹 ！！
# @FileName: settings.py
# @Software: PyCharm

import os

BASE_PATH = os.path.dirname(
    os.path.dirname(__file__)
)

DB_PATH = os.path.join(
    BASE_PATH, 'db'
)