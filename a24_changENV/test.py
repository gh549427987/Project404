# coding: utf-8
# @Time    : 2020/7/8 11:45 下午
# @Author  : 蟹蟹 ！！
# @FileName: test..py
# @Software: PyCharm

import winreg

_delkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\NetVios\NetViosVR\Games')
winreg.DeleteKey(_delkey, 'VR000001')