# coding: utf-8
# @Time    : 2020/7/8 16:53
# @Author  : 蟹蟹 ！！
# @FileName: a24_changeENV.py
# @Software: PyCharm

import winreg
import logging
import json
import re
from conf import conf
import os

#
with open('conf/settings.json', 'r') as f:
    envReg = json.load(f)


class regOperator():
    '''
        注册表Game目录下不要由sub——key
        操作保存当前注册表信息，生成新的注册表
        设置选定环境的注册表信息
    '''

    def __init__(self,envtype='',pathGameReg=envReg['EnvReg']["pathGameReg"],
                 pathPlatformReg=envReg['EnvReg']["pathPlatformReg"],
                 pathPluginsReg=envReg['EnvReg']["pathPluginsReg"]):
        self.pathGameReg = pathGameReg
        self.pathPlatformReg = pathPlatformReg
        self.pathPluginsReg = pathPluginsReg
        self.envType = envtype
        self.oldtype = old_type

        self.pathGameKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.pathGameReg)
        self.pathPlatformKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.pathPlatformReg)
        self.pathPluginsKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.pathPluginsReg)

        # 不同版本的安装路径
        self.platformInstallPath_Default = envReg['platform_Default']['InstallPath']
        self.platformInstallPath_Online = envReg['platform_Online']['InstallPath']
        self.platformInstallPath_Test = envReg['platform_Test']['InstallPath']
        # 调用自己的类方法，确认当前版本
        # self.oldtype = self.currentVersion


    # 判断当前版本
    def currentVersion(self):
        _l = {}
        name, value, type = winreg.QueryValue(self.pathPlatformKey, 'InstallPath')
        _l[name] = value
        if _l['InstallPath'] == self.platformInstallPath_Default:
            return 'Default'
        elif _l['InstallPath'] == self.platformInstallPath_Online:
            return 'Online'
        elif _l['InstallPath'] == self.platformInstallPath_Test:
            return 'Test'
        else:
            print('Can\'t not identify current Version！Please check setting.json')
            return None

    # 删除Games目录下注册表
    def del_games(self):
        i = 0
        _gamelist = []
        while True:
            try:
                d = winreg.EnumKey(self.pathGameKey, i)
                _gamelist.append(d)
                i += 1
            except :
                print('del_games First step Done!')
                break
        print(_gamelist)

        for game in _gamelist:
            print(game)
            print(self.pathGameReg+'\\'+game)
            _delkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.pathGameReg)
            winreg.DeleteKey(_delkey, game)
            i+=1
        print("游戏注册表删除完成！")
    # 注入注册表
    def setReg(self):
        with open('{}/{}_latest.json'.format(conf.REG_PATH, self.envType),'r') as f:
            _reg = json.load(f)

        def setGames():
            _setKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.pathGameReg)

            for game in _reg['Games'].keys():
                # 创建每个游戏的注册表
                winreg.CreateKey(_setKey, game[-8:])
                # 填入每个游戏的属性
                for property in _reg['Games'][game].keys():
                    _setvalueKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, game, access=winreg.KEY_SET_VALUE)
                    winreg.SetValueEx(_setvalueKey,property,0,1,_reg['Games'][game][property])
        def setPlatform():
            for property in _reg['platform'].keys():
                winreg.SetValueEx(self.pathPlatformKey,property,0,1,_reg[property])
        def setPlugins():
            for property in _reg['Plugins'].keys():
                winreg.SetValueEx(self.pathPluginsKey, property, 0, 1, _reg[property])

        try:
            setGames()
            setPlatform()
            setPlugins()
            print('注册表注入成功')
        except:
            print('注册表注入失败')
    # 备份当前注册表
    def saveReg(self,oldtype):
        """
        {  _all
            "game_":{   _lp
                "VR00001":{   _l
                    "properties":'pppp'
                    "properties":'pppp'
                    "properties":'pppp'
                    ...
                }
            }
        }
        :return:
        """
        _all = {}
        # ==================================================
        # save the reg into json file
        # _lp save game by game reg data
        # 闭包函数
        # 读取游戏注册表
        def readGames():
            # gain gamelist reg
            gameRegList = []
            gamecount = 0
            gameID = []
            # iterate game list register,gain all the reg file name
            while True:
                try:
                    gameNum = winreg.EnumKey(self.pathGameKey, gamecount)
                    gamespath = self.pathGameReg + '\\' + gameNum
                    gamecount += 1
                    gameID.append(gameNum)  # gain ID list of every game
                    gameRegList.append(gamespath)
                except:
                    print("saveReg: gamelist is Finished")
                    break

            _lp = {}
            for path in gameRegList:
                # path = re.search('[^\\/:*?"<>|\r\n]+$', path).group()
                # print(path)
                _lp[path] = {}  # 创建当前游戏id 的字典
                gamekey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)
                # _l save key and value one by one
                _l = {}
                _l_count = 0
                try:
                    while True:
                        name, value, type = winreg.EnumValue(gamekey, _l_count)
                        # create key：value str
                        _l[name]=value     #  创建当前游戏内，所有属性噶字典
                        _l_count+=1
                except:
                    # create game's name with key:value str
                    # "game":{key:value}
                    _lp[path] = _l  # 赋值到当前游戏id到字典内
                    print('{}\'s reg has been added'.format(path[-8:]))

            # create all games reg str
            return _lp
        # 读取平台注册表
        def readPlatform():
            _l = {}
            _l_count=0
            try:
                while True:
                    name, value, type = winreg.EnumValue(self.pathPlatformKey, _l_count)
                    # create key：value str
                    _l[name] = value  # 创建当前游戏内，所有属性噶字典
                    _l_count += 1
            except:
                print('Platforms\'s reg has been added')
            return _l
        # 读取插件注册表
        def readPlugins():
            _l = {}
            _l_count = 0
            try:
                while True:
                    name, value, type = winreg.EnumValue(self.pathPluginsKey, _l_count)
                    # create key：value str
                    _l[name] = value  # 创建当前游戏内，所有属性噶字典
                    _l_count += 1
            except:
                print('Plugins\'s reg has been added')
            return _l

        _all['Games'] = readGames()
        _all['platform'] = readPlatform()
        _all['Plugins'] = readPlugins()
        # save all the str into a file with json
        with open('{}/{}_latest.json'.format(conf.REG_PATH,oldtype), 'w') as f:
            json.dump(_all, f, ensure_ascii=False, indent=2)




# 一键切换流程
def run(envtype):
    ro = regOperator(envtype=envtype)
    ver = ro.currentVersion() # 先判断当前版本

    if ver: # 如果当前版本能够识别
        # 如果已经是新版本，打印信息
        if ver == envtype:
            print(f'Current version is {envtype}!')
        # 如果是旧版本，执行备份——》更新注册表路径
        else:
            print(f'To {envtype} begin~')
            print('备份当前注册表')
            # 备份当前注册表
            ro.saveReg(oldtype=ver)
            # 初始化当前游戏注册表
            ro.del_games()
            # 注入正式环境注册表
            ro.setReg()
    # 打开launcher
    exe_path = envReg[f'platform_{envtype}'] + '\\NetviosVR.exe'
    os.open(exe_path)


def toOnline():
    run('Online')

def toTest():
    run('Test')

def toDefault():
    run('Default')

def currentVersion():
    ver = regOperator().currentVersion()
    if ver:
        print(f"当前环境是{ver}")
    return None

def saveReg():
    ro = regOperator()
    ver = ro.currentVersion()
    if ver:
        ro.saveReg(ver)
    else:
        print('注册表保存失败！')


