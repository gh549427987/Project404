# coding: utf-8
# @Time    : 2020/7/8 16:53
# @Author  : 蟹蟹 ！！
# @FileName: a24_changeENV.py
# @Software: PyCharm

from conf import conf
from resource.regOperator import regOperator
import logging
import os

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)

# 一键切换流程
def run(envtype):
    ro = regOperator(envtype=envtype)
    ver = ro.currentVersion() # 先判断当前版本
    exe_path = str(conf.envReg[f'platform_{envtype}']['InstallPath']) + '\\NetviosVR.exe' # 创建launcher启动路径
    if ver: # 如果当前版本能够识别
        # 如果已经是新版本，打印信息
        if ver == envtype:
            logging.info(f'Current version is {envtype}!')
            os.system(exe_path)
        # 如果是旧版本，执行备份——》更新注册表路径
        else:
            logging.info(f'To {envtype} begin~')
            logging.info('备份当前注册表')
            # 备份当前注册表
            logging.info("================== Execute saveREG ==================")
            ro.saveReg(oldtype=ver)
            logging.info("================== Finish saveREG ==================")
            # 初始化当前游戏注册表
            logging.info("================== Execute init_gameREG ==================")
            ro.del_games()
            logging.info("================== Finish init_gameREG ==================")
            # 注入环境注册表
            logging.info("================== Execute setREG ==================")
            ro.setReg()
            logging.info("================== Finish setREG ==================")
            os.system(exe_path)

def toOnline():
    run('Online')

def toTest():
    run('Test')

def toDefault():
    run('Default')

def currentVersion():
    ro = regOperator()
    ver = ro.currentVersion()
    if ver:
        logging.info('============= Excute current version =============')
        logging.info(f"当前环境是{ver}")
        logging.info('============= Finish current version =============')
    return None

def saveReg():
    ro = regOperator()
    logging.info("================== Execute saveREG ==================")
    ver = ro.currentVersion()
    if ver:
        ro.saveReg(ver)
    else:
        logging.info('注册表保存失败！')
    logging.info("================== Finish saveREG ==================")

