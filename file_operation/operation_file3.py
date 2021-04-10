# !/usr/local/bin/ python3
# -*- coding:utf-8 -*-
"""
    open函数指定"t"的文本格式，encoding指定编码格式
"""
# 字符串默认编码就是unicode
s = '高羲之'

f = open('../files/fileWrite3.txt', 'wt', encoding='utf8')
f.write(s)
f.close()

f = open('../files/fileWrite3.txt', 'rt', encoding='utf8')
t = f.read()
print(t)
# print(t.decode('gbk'))
