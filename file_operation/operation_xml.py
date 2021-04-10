# !/usr/local/bin/ python
# -*- coding:utf-8 -*-

"""
    解析xml文档
    使用标准库中的xml.etree.ElementTree其中的parse函数可以解析xml文档
    使用标准库中的xml.etree.ElementTree构建ElementTree，使用write方法写入文件
"""
import csv
from xml.etree.ElementTree import parse, Element, tostring, ElementTree

f = open('../files/shengxiao.xml')

et = parse(f)

root = et.getroot()
# 当前子节点操作
for child in root:
    print(child.get('name'))

print(root.find('shengxiao'))

print(root.findall('target'))

# 所有子节点操作
print("""-所有子节点操作-""")
for i in root.iter():
    print(i.get('name'))

root.iterfind('target')
for e in root.iterfind('target'):
    print(e.get('name'))

#
for e in root.iter('maps'):
    print(e.get('id'))
# 使用通配符号

# 匹配xparam下所有对于root的孙子节点
for x in root.findall('xparam/*'):
    print(x.get('id'))

# 匹配无论在任何位置的maps节点
root.findall('.//maps')
# 指定标签名称
print(root.findall('target[@name="clean"]'))
# 指定多个相同节点的指定位置，起始值为1
print(root.find('xparam').findall('maps[1]'))
print(root.find('xparam').findall('maps[2]'))
# 倒数第二个
print(root.find('xparam').findall('maps[last()-1]'))
# 指定节点属性
print(root.find('xparam').findall('maps[id="01"]'))
# 指定节点内容
print(root.findall('xparam[maps="牛"]'))

"""
    csv文档转换为xml格式
"""
e = Element('data')
# 节点标签
print(e.tag)
e.set('name', 'gaox')
print(tostring(e))
e.text = 'gaoxizhi'
print(tostring(e))

# 添加子元素
e2 = Element('age')
e2.text = '23'
e3 = Element('work')
e.append(e2)
e.append(e3)
print(tostring(e))


def csvToXml(fname):
    with open(fname, 'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()

        root = Element('data')
        for row in reader:
            eRow = Element('row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
        return ElementTree(root)


et = csvToXml('../files/yi.csv')

et.write('../files/data.xml')

"""
   xml文件格式化 1
"""


def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level

tree = parse('../files/data.xml')  # 解析data.xml这个文件
root = tree.getroot()  # 得到根元素，Element类
pretty(root)  # 执行美化方法
tree.write('../files/data1.xml')


"""
   xml文件格式化 2
"""


def pretty_xml(element, indent, newline, level=0):  # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
    if len(element):  # 判断element是否有子元素
        if (element.text is None) or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
            # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
            # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element)  # 将element转成list
    for sub_element in temp:
        if temp.index(sub_element) < (len(temp) - 1):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
            sub_element.tail = newline + indent * (level + 1)
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
            sub_element.tail = newline + indent * level
        pretty_xml(sub_element, indent, newline, level=level + 1)  # 对子元素进行递归操作


tree = parse('../files/data.xml')  # 解析data.xml这个文件
root = tree.getroot()  # 得到根元素，Element类
pretty_xml(root, '\t', '\n')  # 执行美化方法
tree.write('../files/data2.xml')
