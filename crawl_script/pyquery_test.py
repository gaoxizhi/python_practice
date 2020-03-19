#-*-encoding=utf-8-*-

from pyquery import PyQuery as pq
import requests

# 推荐使用方式（爬取数据使用urllib嚯requests，pyquery主要负责解析数据）

res = requests.get("http://www.baidu.com")
res.encoding = "utf-8"
doc = pq(res.text)
print(doc('title'))

# 读取my.html信息
f = open("my.html", "r", encoding="utf-8")
content = f.read()
f.close()

# 使用pyquery解析网页
doc = pq(content)

# 解析网页内容，使用选择器
print(doc("h3"))
# 获取id属性值为hid的标签节点
print(doc("#hid"))
# 获取class属性值为shop的所有标签节点
print(doc(".shop"))
print(doc("li a"))

print(doc("li:first"))
print(doc("li:last"))
# 获取网页中第三个li标签
print(doc("li:eq(2)"))

print("=" * 32)
# 二次筛选，子标签
print(doc("li"))
print(doc("li").find("p"))

alist = doc("a")

for a in alist.items():
    # a.text() 等同于 a.html()
    print("内容：", a.text(), "，地址：", a.attr("href"), "。")
