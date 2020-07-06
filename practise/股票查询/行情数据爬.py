# coding: utf-8
# @Time    : 2020/7/4 2:17 上午
# @Author  : 蟹蟹 ！！
# @FileName: 行情数据爬.py
# @Software: PyCharm

from selenium import webdriver
import logging
import time

logger = logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %('
                                                         'levelname)s: %(message)s')
# 无界面执行
# option = webdriver.ChromeOptions()
# option.add_argument('headless')

# th[1]/div/span 从末尾的1到23
titlelocation = '#hsRank > div.ID_tabs.clearfix > div.tabs-pane.pane-border.current > div > div.panelscroll-v > div.panelscroll-h > div.viewport > div > div > table.table-header > thead > tr > th:nth-child(1) > div > span'
# table[2]/tbody/tr[1]/td[1] td[1]到td[23] tr[1]到tr[24]
data_1 = '//*[@id="hsRank"]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div/table[2]/tbody/tr[1]/td[1]'
data_2 = '//*[@id="hsRank"]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div/table[2]/tbody/tr[1]/td[2]/a'
data_3 = '//*[@id="hsRank"]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div/table[2]/tbody/tr[1]/td[3]/a'
data_3_1 = '//*[@id="hsRank"]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div/table[2]/tbody/tr[2]/td[3]/div/a[1]'
data_other = '//*[@id="hsRank"]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div/table[2]/tbody/tr[1]/td[4]'

url = 'http://quotes.money.163.com/old/#query=hy012001&DataType=HS_RANK&sort=PERCENT&order=desc&count=24&page=0'
broswer = webdriver.Safari()
broswer.get(url)
broswer.implicitly_wait(3)
with open('stock_data.txt', 'w') as f:

    # 先读取title
    title_list = []
    data_list = []
    for i in range(1,24):
        title = broswer.find_element_by_css_selector(titlelocation.replace(titlelocation[-15], str(i))).text
        f.write(title.center(10, ' '))
    f.write('\n')
    try:
        # 逐行写入其他数据
        for row in range(1,24):
            # 每次清空data_list
            data_list.clear()

            data_list.append(broswer.find_element_by_xpath(data_1[:-8] + '%d'%row +data_1[-7:]).text)
            data_list.append(broswer.find_element_by_xpath(data_2[:-10] + '%d'%row +data_2[-9:]).text)
            try:
                data_list.append(broswer.find_element_by_xpath('//*[@id="hsRank"]/div[2]/div[3]/div/div[1]/div['
                                                               '2]/div[2]/div/div/table[2]/tbody/tr[%d]/td[3]/a['
                                                               '1]'%row).text)
            except:
                data_list.append(broswer.find_element_by_xpath('//*[@id="hsRank"]/div[2]/div[3]/div/div[1]/div['
                                                               '2]/div[2]/div/div/table[2]/tbody/tr[%d]/td[3]/div/a['
                                                               '1]'%row).text)
            for i in range(4,24):
                 data = broswer.find_element_by_xpath('//*[@id="hsRank"]/div[2]/div[3]/div/div[1]/div[2]/div['
                                                      '2]/div/div/table[2]/tbody/tr[%d]/td[%d]'%(row,i)).text
                 data_list.append(data)

            for i in data_list:
                f.write(i.center(10, ' '))
            f.write('\n')
    except:
        broswer.close()

broswer.close()

