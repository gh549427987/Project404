# coding: utf-8
# @Time    : 2020/7/8 16:53
# @Author  : 蟹蟹 ！！
# @FileName: a24_changeENV.py
# @Software: PyCharm

import winreg
import logging
import json


logger = logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %('
                                                         'levelname)s: %(message)s')

class regOperator():
    '''
        操作保存当前注册表信息，生成新的注册表
        设置选定环境的注册表信息
    '''

    def __init__(self,pathGameReg,pathPlatformReg,pathPluginsReg):
        self.pathGameReg = pathGameReg
        self.pathPlatformReg = pathPlatformReg
        self.pathPluginsReg = pathPluginsReg

    def setReg(self):
        with open('test.json', 'r') as f :
            print(json.load(f)

        pass

    def saveReg(self):
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
        pathGameKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.pathGameReg)
        pathPlatformKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.pathPlatformReg)
        pathPluginsKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.pathPluginsReg)

        games_dicreg = {}
        platform_dicreg = {}
        plugins_dicreg = {}
        all_list = []
        save_json = ''


        # gain gamelist reg
        gameRegList = []
        gamecount = 0
        gameID = []
        # iterate game list register,gain all the reg file name
        while True:
            try:
                gameNum = winreg.EnumKey(pathGameKey, gamecount)
                gamespath = self.pathGameReg + '\\' + gameNum
                gamecount+=1
                gameID.append(gameNum) # gain ID list of every game
                gameRegList.append(gamespath)
            except:
                print("saveReg: gamelist is Finished")
                break

        # ==================================================

        # save the reg into json file
        # _lp save game by game reg data
        _all = {}
        _lp = {}
        for path,gameid in gameRegList,gameID:
            _lp[gameid] = {}  # 创建当前游戏id 的字典
            gamekey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)
            # _l save key and value one by one
            _l = {}
            for i in range(len(gameRegList)):
                name, value, type = winreg.EnumValue(gamekey, i)
                # create key：value str
                _l[name]=value     #  创建当前游戏内，所有属性噶字典
            # create game's name with key:value str
            # "game":{key:value}
            _lp[gameid] = _l # 赋值到当前游戏id到字典内
        # create all games reg str

        _all['Game'] = _lp
        # save all the str into a file with json
        with open('test.json', 'w') as f:
            json.dump(_all, f, ensure_ascii=False, indent=2)


# load settings
def settings(Env):
    ''':arg load settings data from settings.json'''

    with open('settings.json','r') as f:
        data = json.load(f)
    if Env == 'Online':
        envReg = data['onlineEnvReg']
    elif Env == 'Test':
        envReg = data['testEnvReg']
    else:
        print("环境选择错误")
        return 0
    return envReg

# choose environment
def chooseEnv():

    # 选择切换到正式环境或者测试环境
    while True:
        #envChoose = input("choose a Env you want to change(1:Online while 2:Test) >> ").strip()
        envChoose = '1'
        if envChoose == '1':
            return(settings('Online'))
        elif envChoose == '2':
            return(settings('Test'))
        elif envChoose == 'quit':
            break
        else:
            continue

# main
def main():
    # 选择切换
    envReg = chooseEnv()
    ro = regOperator(pathGameReg=envReg["pathGameReg"],
                pathPlatformReg=envReg["pathPlatformReg"],
                pathPluginsReg=envReg["pathPluginsReg"])
    # ro.saveReg()
    ro.setReg()



if __name__ == '__main__':
    main()

