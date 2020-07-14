# coding: utf-8
# @Time    : 2020/7/14 20:17
# @Author  : 蟹蟹 ！！
# @FileName: regOperator.py
# @Software: PyCharm
import json
import winreg
from conf import conf
import time
import os
import logging

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)


# 注册表操作
class regOperator():
    '''
        注册表Game目录下不要由sub——key
        操作保存当前注册表信息，生成新的注册表
        设置选定环境的注册表信息
    '''

    def __init__(self,envtype='',pathGameReg=conf.envReg['EnvReg']["pathGameReg"],
                 pathPlatformReg=conf.envReg['EnvReg']["pathPlatformReg"],
                 pathPluginsReg=conf.envReg['EnvReg']["pathPluginsReg"]):
        self.pathGameReg = pathGameReg
        self.pathPlatformReg = pathPlatformReg
        self.pathPluginsReg = pathPluginsReg
        self.envType = envtype

        self.pathGameKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.pathGameReg)
        self.pathPlatformKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.pathPlatformReg, access=winreg.KEY_ALL_ACCESS)
        self.pathPluginsKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.pathPluginsReg, access=winreg.KEY_ALL_ACCESS)

        # 不同版本的安装路径
        self.platformInstallPath_Default = conf.envReg['platform_Default']['InstallPath']
        self.platformInstallPath_Online = conf.envReg['platform_Online']['InstallPath']
        self.platformInstallPath_Test = conf.envReg['platform_Test']['InstallPath']
        # 调用自己的类方法，确认当前版本
        # self.oldtype = self.currentVersion


    # 判断当前版本
    def currentVersion(self):
        _l = {}
        value, type= winreg.QueryValueEx(self.pathPlatformKey, 'InstallPath')
        _l['InstallPath'] = value
        if _l['InstallPath'] == self.platformInstallPath_Default:
            return 'Default'
        elif _l['InstallPath'] == self.platformInstallPath_Online:
            return 'Online'
        elif _l['InstallPath'] == self.platformInstallPath_Test:
            return 'Test'
        else:
            logging.error('Can\'t not identify current Version！Please check setting.json')
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
                logging.error('del_games First step Done!')
                break

        for game in _gamelist:
            logging.info(game)
            _delkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.pathGameReg)
            winreg.DeleteKey(_delkey, game)
            i+=1
        logging.info("游戏注册表删除完成！")
    # 注入注册表
    def setReg(self):
        with open('{}\{}_env\{}_latest.json'.format(conf.REG_PATH, self.envType, self.envType),'r') as f:
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
                winreg.SetValueEx(self.pathPlatformKey,property,0,1,_reg['platform'][property])
        def setPlugins():
            _l = {}
            i = 0
            # 检查一下plugin目录有多少个插件
            while True:
                try:
                    name, value = winreg.EnumKey(self.pathPluginsKey,i)
                    _l[name] = value
                    i+=1
                except:
                    break
            if not _l:# 如果插件下有插件，逐个插入
                for key in _l.keys():
                    _pluginKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.pathPluginsReg+'\\'+ key,
                                                access=winreg.KEY_WRITE)
                    for property in _reg['Plugins'].keys():
                        winreg.SetValueEx(_pluginKey, property, 0 , 1, _reg[self.pathPluginsReg])
                logging.info('插件注入完成')
            else:
                logging.info('插件注入完成')
                pass

        try:
            setGames()
            setPlatform()
            setPlugins()
            logging.info('注册表注入成功')
        except:
            logging.error('注册表注入失败')
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
                    logging.error("saveReg: gamelist is Finished")
                    break

            _lp = {}
            for path in gameRegList:
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
                    logging.error('saveReg:{}\'s reg has been added'.format(path[-8:]))

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
                logging.error('saveReg:Platforms\'s reg has been added')
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
                logging.error('saveReg:Plugins\'s reg has been added')
            return _l

        _all['Games'] = readGames()
        _all['platform'] = readPlatform()
        _all['Plugins'] = readPlugins()
        # save all the str into a file with json
        _regJson = '{}\{}_env\{}_latest.json'.format(conf.REG_PATH,oldtype,oldtype)
        curr_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        _regBackup = '{}\{}_env\{}_{}.json'.format(conf.REG_PATH, oldtype, oldtype, curr_time)
        with open(_regJson, 'w') as f:
            json.dump(_all, f, ensure_ascii=False, indent=2)
        os.system('copy {} {}'.format(_regJson, _regBackup))
        

if __name__ == '__main__':
    ro = regOperator('Online')
    ver = ro.currentVersion()
    ro.saveReg(ver)
