# coding: utf-8
# @Time    : 2020/7/2 16:08
# @Author  : 蟹蟹 ！！
# @FileName: p11.py
# @Software: PyCharm
def last2(str):
  index = str[:2]
  count = 0
  for i in range(len(str)-1):
    print(str[i:i+1])
    if index == str[i:i+1]:
      count += 1
  return count
print('code'[:1])

def last2(str):
  if len(str)<2:
    return 0
  index = str[:2]
  end = str[-2:]
  count = 0
  for i in range(len(str)-1):
    if index == str[i:i+2]:
      count += 1
  if index == end:
    return count-1
  return count