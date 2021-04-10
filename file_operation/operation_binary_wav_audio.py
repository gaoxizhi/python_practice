# !/usr/local/bin/ python3
# -*- coding:utf-8 -*-

"""
    处理二进制文件
    例如wav格式文件，读取部分信息
    python2可以使用，python3在(0 for _ in range(n))处类型错误：生成器为浮点型

    open函数以二进制模式打开文件，指定mode参数为'b'，
    二进制数据可以用readinto，读入到提前分配好的buffer中，便于数据处理，
    解析二进制数据可以使用标准库中的struct模块的unpack方法。
"""
import array
import struct

f = open('../files/渔舟唱晚.wav', 'rb')

info = f.read(44)
print(info)

print(struct.unpack('h', b'\x01\x02'))
# 大端
print(struct.unpack('>h', b'\x01\x02'))

s1 = struct.unpack('h', info[22:24])
s2 = struct.unpack('i', info[24:28])
s3 = struct.unpack('h', info[34:36])

print(s1)
print(s2)
print(s3)

# 文件长度
print(f.seek(0, 2))
print(f.tell())
# for循环时要求次数为整数
n = int((f.tell() - 44) / 2)
buf = array.array('h', (0 for _ in range(n)))
# 文件指针
f.seek(44)
# 数据载入
f.readinto(buf)
for i in range(n):
    buf[i] = int(buf[i] / 8)
f2 = open('渔舟唱晚2.wav', 'wb')

f2.write(info)
buf.tofile(f2)
f2.close()
