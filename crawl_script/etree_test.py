# -*-encoding=utf-8-*-
from lxml import etree

# 读取html文件信息
f = open('my.html', "r", encoding="utf-8")
content = f.read()
f.close()

# 初始化解析html文档，并返回根节点对象
html = etree.HTML(content)

# 获取title节点对象
result = html.xpath("/html/head/title/text()")
print(",".join(result))
# 获取h3标签内容
result = html.xpath("/html/body/h3/text()")
print(",".join(result))
# 获取h3标签的id
result = html.xpath("/html/body/h3/@id")
print(",".join(result))
# 获取html/body/ul下的所有li节点
result = html.xpath("/html/body/ul/li")
print(result)
# 获取网页中所有li元素节点
result = html.xpath("//li")
print(result)

# 批量获取
result = html.xpath("//li/a/text()")
# 获取链接属性
result = html.xpath("//li/a/@href")

print(result)

print("--" * 32)

# 按序选择
# 第一个li中的a标签文本内容
result = html.xpath("//ul/li[1]/a/text()")
# 最后一个a
result = html.xpath("//ul/li[last()]/a/text()")
# 前两个
result = html.xpath("//ul/li[position()<3]/a/text()")
# 从后数第三个
result = html.xpath("//ul/li[last()-2]/a/text()")

# 节点轴选择
# 获取第一个li中a节点的所有祖先节点
result = html.xpath("//li[1]/a/ancestor::*")
# 获取第一个li中a节点的ul祖先节点
result = html.xpath("//li[1]/a/ancestor::ul")
# 获取第三个li中a节点的所有属性
result = html.xpath("//li[3]/a/attribute::*")
# 获取属性class属性值为aa的所有节点
result = html.xpath("//li/a[@class='aa']/text()")
# tbody的所有子节点
result = html.xpath("//table/tbody/child::tr[@class='tt']")

# 节点遍历（多层解析）
result = html.xpath("//li/a")
for v in result:
    print(v.xpath("text()")[0] + ":" + v.xpath("@href")[0])
    print(v.text + ":" + v.get('href'))
