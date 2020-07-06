# coding: utf-8
# @Time    : 2020/7/4 3:13 上午
# @Author  : 蟹蟹 ！！
# @FileName: settings.py.py
# @Software: PyCharm

# th[1]/div/span 从末尾的1到23
titlelocation = '#hsRank > div.ID_tabs.clearfix > div.tabs-pane.pane-border.current > div > div.panelscroll-v > div.panelscroll-h > div.viewport > div > div > table.table-header > thead > tr > th:nth-child(1) > div > span'

# table[2]/tbody/tr[1]/td[1] td[1]到td[23] tr[1]到tr[24]
datalocation =  '/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div/table[2]/tbody/tr[1]/td[1]'

# print(datalocation[-2])
# print(datalocation[-8])

datalocation =  '#hsRank > div.ID_tabs.clearfix > div.tabs-pane.pane-border.current > div > div.panelscroll-v > div.panelscroll-h > div.viewport > div > div > table.ID_table.stocks-info-table > tbody > tr:nth-child(1) > td.xh-highlight'

data_1 = '//*[@id="hsRank"]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div/table[2]/tbody/tr[1]/td[1]'
data_2 = '//*[@id="hsRank"]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div/table[2]/tbody/tr[1]/td[2]/a'
data_3 = '//*[@id="hsRank"]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div/table[2]/tbody/tr[1]/td[3]/a'
data_other = '//*[@id="hsRank"]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div/table[2]/tbody/tr[1]/td[4]'
a= '序号,代码,名称,价格,涨跌幅,涨跌额,5分钟涨跌额,今开,昨收,最高,最低,成交量,成交额,换手率,量比,委比,振幅,市盈率,流通市值,总市值,每股收益,净利润,主营收'.split(',')
b = '序号,代码,名称,价格,涨跌幅,涨跌额,5分钟涨跌额,今开,昨收,最高,最低,成交量,成交额,换手率,量比,委比,振幅,市盈率,流通市值,总市值,每股收益,净利润,主营收'
for i in a:
    print(i.ljust(8, ' '))
print(''.center())