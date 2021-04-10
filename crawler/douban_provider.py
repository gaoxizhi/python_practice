#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import re
from urllib import request

import xlwt

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
url = "https://read.douban.com/provider/all"

# 可以使用urllib.request.build_opener()进行
# 也可以使用urllib.request.Request()下的add_header()实现浏览器的模拟。
req = request.Request(url, None, headers)
html = request.urlopen(req, timeout=2).read()  # 读取网页源代码内容
wzgz = "<a href=\"(.*?)\" class=\"provider-item\"><div class=\"col-media\"><div class=\"cm-left avatar\"><div class=\"avatar\"><img src=\"(.*?)\"/></div></div><div class=\"cm-body\"><div class=\"name\">(.*?)</div><div class=\"works-num\">(.*?) 部作品在售</div></div></div></a>"
xx = re.compile(wzgz).findall(str(html, "utf-8"))  # 通过正则表达式匹配在网页源代码中提取所需内容
print(xx)

# 创建workbook和sheet对象
workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)

# 初始化excel样式
style = xlwt.XFStyle()

# 为样式创建字体
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True

# 设置样式的字体
style.font = font

# 在sheet1表的第1行设置字段名称并写入数据
sheet1.write(0, 0, "序号", style)
sheet1.write(0, 1, "出版社-URL", style)
sheet1.write(0, 2, "LOGO-URL", style)
sheet1.write(0, 3, "出版社名称", style)
sheet1.write(0, 4, "在售作品数量", style)

a = 0  # 定义行号初始值
h = 0  # 定义在售数量初始值
for i in xx:
    # print(str(a+1),i[0])
    sheet1.write(a + 1, 0, a + 1, style)  # 在第a+1行第1列写入序号
    sheet1.write(a + 1, 1, "https://read.douban.com" + str(i[0]), style)  # 在第a+1行第2列写入出版社URL
    sheet1.write(a + 1, 2, i[1], style)  # 在第a+1行第3列写入LOGO-URL
    sheet1.write(a + 1, 3, i[2], style)  # 在第a+1行第4列写入出版社名称
    sheet1.write(a + 1, 4, int(i[3]), style)  # 在第a+1行第5列写入在售数量
    h += int(i[3])  # 在售数量累计求和
    a += 1

    if a == a:  # 判断XX列表是否遍历结束，并在sheet1表尾行写入在售数量求和的值
        t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        t1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        sheet1.write(a + 1, 3, "合计", style)  # 在sheet1表尾行写入“合计”
        sheet1.write(a + 1, 4, h, style)  # 在sheet1表尾行写入在售数量累计值
        sheet1.write(a + 2, 3, "采集时间", style)  # 在sheet1表尾行写入数据采集时间
        sheet1.write(a + 2, 4, t, style)  # 在sheet1表尾行写入数据采集时间

workbook.save("../files/豆瓣出版社汇总表" + str(t1) + ".xls")  # 保存该excel文件,有同名文件时无法直接覆盖

print("数据写入excel文件完毕！")
print("在售书数量合计：" + str(h))
