# !/usr/local/bin/ python
# -*- coding:utf-8 -*-


"""
    写入文件前对unicode编码，读入文件后对二进制字符串解码
"""

s = u'高羲之'
# \xb8\xdf\xf4\xcb\xd6\xae
print(s.encode('gbk'))
# \xe9\xab\x98\xe7\xbe\xb2\xe4\xb9\x8b
print(s.encode('utf8'))

# 将gbk编码按照utf8输出，可能抛出异常UnicodeDecodeError: invalid start byte
# print('\xb8\xdf\xf4\xcb\xd6\xae'.decode('utf8'))
# 将utf8编码按照gbk输出，可能抛出异常UnicodeDecodeError: incomplete multibyte sequence
# print('\xe9\xab\x98\xe7\xbe\xb2\xe4\xb9\x8b'.decode('gbk'))

f = open('fileWrite.txt', 'w')
f.write(s.encode('gbk'))
f.close()

f = open('fileWrite.txt', 'r')
t = f.read()
print(t)
print(t.decode('gbk'))
