#-*-encoding=utf-8-*-
from bs4 import BeautifulSoup

#读取html文件信息
f = open('my.html', "r", encoding="utf-8")
content = f.read()
f.close()

# 初始化解析html文档，并返回根节点对象
soup = BeautifulSoup(content, "lxml")
# html文档的格式化信息
# print(soup.prettify())

# 节点选择器的解析
# 第一个ll节点；
print(soup.li)
# 第一个a标签：所有属性，地址
print(soup.a.attrs, " , ", soup.a.attrs['href'])
# 节点文本内容，节点名（标签）
print(soup.li.a.string, " , ", soup.li.a.name)

# 获取网页第一个li节点
print(soup.find(name="li"))
print(soup.find(name="a"))
# 获取第一个class属性为aa的节点
print(soup.find(attrs={'class': 'aa'}))
print(soup.find_all(attrs={'class': 'aa'}))
# 获取所有class属性值为aa的a标签节点
print(soup.find_all(name='a', attrs={'class': 'aa'}))
print(soup.find_all(text='li1'))

# css选择器
# 获取所有li节点
print(soup.select("li"))
# 获取id属性值为hid的节点
print(soup.select("#hid"))
# 获取所有class属性值为shop的节点
print(soup.select(".shop"))

nodes = soup.select("ul li a")
for v in nodes:
    # print(v['href']+":"+v.string)
    print(v.attrs['href'] + ";" + v.get_text())
