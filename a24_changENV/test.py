# coding: utf-8
# @Time    : 2020/7/8 11:45 下午
# @Author  : 蟹蟹 ！！
# @FileName: test..py
# @Software: PyCharm

import json

with open('test.json', 'r') as f:
    data = f.read()
    data = data.replace('\\\"','\"')
    data = data.replace('\\\\','\\\\\\\\')
    print(data)
    js = eval(data)
    print(type(js))
print(js)
print(type(js))
print(json.dumps(js))
print(type(js))
with open('test_2.json', 'w') as f:
    json.dump(js,f,indent=2)

with open('test_3.json', 'w') as f:
    f.write(js)

with open('test_4.json', 'w') as f:
    f.write(js)
    pass
j = {"Softwaare\\NetVios\\NetViosVR\\Games\\VR000001":{"GAME_ID":"VR000001","":"","NAME":"Creed：荣耀擂台","VERSION":"1.0.0","STARTUP_PATH":"\\Creed\\11112019_CR_Netvios_186719_sdk\\186719\\WindowsNoEditor\\Creed.exe","GAME_LEVEL":"SR","SIZE":"2809058630","CHECKSUM":"cbc07e7c06a2443c7fad4bf4e2ae4fa6","FORCE_UPDATE":"false"}}
js = {"Softwaare\\NetVios\\NetViosVR\\Games\\VR000001":{"GAME_ID":"VR000001","":"","NAME":"Creed：荣耀擂台","VERSION":"1.0.0","STARTUP_PATH":"\\Creed\\11112019_CR_Netvios_186719_sdk\\186719\\WindowsNoEditor\\Creed.exe","GAME_LEVEL":"SR","SIZE":"2809058630","CHECKSUM":"cbc07e7c06a2443c7fad4bf4e2ae4fa6","FORCE_UPDATE":"false"},"Software\\NetVios\\NetViosVR\\Games\\VR000002":{"GAME_ID":"VR000002","":"","NAME":"怒海远征","VERSION":"0.0.5","STARTUP_PATH":"\\nuhaiyuanzheng\\09172019_BC_Netease_180848\\180848_Client\\WindowsNoEditor\\BroadSides.exe","GAME_LEVEL":"R","SIZE":"3709433293","CHECKSUM":"4df8daf18ce72cbc2155f1979556bc9a","FORCE_UPDATE":"false"},"Software\\NetVios\\NetViosVR\\Games\\VR000004":{"GAME_ID":"VR000004","":"","NAME":"节奏空间","VERSION":"1.1","STARTUP_PATH":"\\Beat Saber\\Beat Saber\\Beat Saber.exe","GAME_LEVEL":"R","SIZE":"506647532","CHECKSUM":"a2c6a471ae77f733f609c78526579358","FORCE_UPDATE":"false"},"Software\\NetVios\\NetViosVR\\Games\\VR000005":{"GAME_ID":"VR000005","NAME":"Raw Data：源代码","VERSION":"1.0.2","STARTUP_PATH":"\\Raw Data\\11272019_RD_NetVios_187307_client\\187307\\WindowsNoEditor\\RawData.exe","GAME_LEVEL":"SR","SIZE":"9102033046","CHECKSUM":"452e974337889799b15fed6e4c48e251","FORCE_UPDATE":"false","DOWNLOAD_URL":"https://a24.gdl.netease.com/1905121445_11272019_RD_NetVios_187307_client.zip"},"Software\\NetVios\\NetViosVR\\Games\\VR000006":{"GAME_ID":"VR000006","":"","NAME":"缤纷泡泡","VERSION":"0.0.2","STARTUP_PATH":"\\GG\\187315\\WindowsNoEditor\\ColorMatch.exe","GAME_LEVEL":"R","SIZE":"855394654","CHECKSUM":"d57c7a4d84c3df7d95e78c9b284e39c1","FORCE_UPDATE":"false"},"Software\\NetVios\\NetViosVR\\Games\\VR000007":{"GAME_ID":"VR000007","NAME":"甜点盛宴","":"","VERSION":"0.2","STARTUP_PATH":"\\DessertSlice\\WindowsNoEditor\\DessertSlice.exe","GAME_LEVEL":"R","SIZE":"493735506","CHECKSUM":"7e9edc8a8ecf47ffa23e77af4451b2cc","FORCE_UPDATE":"false"},"Software\\NetVios\\NetViosVR\\Games\\VR000008":{"GAME_ID":"VR000008","":"","NAME":"竞速达人","VERSION":"1.3","STARTUP_PATH":"\\Sprint Vector\\06262020_SprintVector_207870\\Win64\\WindowsNoEditor\\SprintVector.exe","GAME_LEVEL":"SSR++","SIZE":"6178925732","CHECKSUM":"3d9259486710d06550463f2e1714c9e5","FORCE_UPDATE":"false"},"Software\\NetVios\\NetViosVR\\Games\\VR000012":{"GAME_ID":"VR000012","":"","NAME":"义庄派对","VERSION":"0.2","STARTUP_PATH":"\\yivzhuangpaidui\\VR_Zombie_Netvios_2020.5.12B\\WindowsNoEditor\\VR_Zombie.exe","GAME_LEVEL":"SSR++","SIZE":"738214881","CHECKSUM":"14fe69be14f4be081a3abb83af0dcf39","FORCE_UPDATE":"false"},"Software\\NetVios\\NetViosVR\\Games\\VR000013":{"GAME_ID":"VR000013","":"","NAME":"义庄派对（多人版）","VERSION":"0.3","STARTUP_PATH":"\\yizhuangpaiduiduoren\\VR_Zombie_JJ_Netvios_2020.5.19B\\WindowsNoEditor\\VR_Zombie_JJ.exe","GAME_LEVEL":"R","SIZE":"832170379","CHECKSUM":"45478b95e9d209e915fc5a794d3e8b3c","FORCE_UPDATE":"false"}}
print(type(js))

with open('test_5.json', 'w') as f:
    json.dump(js,f,ensure_ascii=False, indent=2)
# print(json.dumps(j,indent=2))
# print(json.dumps(js,indent=2))

