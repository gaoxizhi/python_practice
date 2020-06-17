"""
f = open("D:/nihao.txt")
print(len(f.read()))
f = open("D:/nihao.txt",'a')
f.write("\n结束：高羲之")
f = open('D:/nihao.txt')
print(len(f.read()))

print(f.read())
"""

# 使用python库爬取网页并存储在本地
from urllib import request

f2 = open("D:/baidu.html", "wb")

data = request.urlopen("http://www.baidu.com")
# print(data.read())
data = data.read()
f2.write(data)
print(len(data))
f2.close()
