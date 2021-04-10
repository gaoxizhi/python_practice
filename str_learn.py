# !/usr/local/bin/ python2
# -*- coding:utf-8 -*-

# 1. 我们要把某个字符串一句分隔符拆分不同的字段，该分隔符包含不同的分隔符
# s = 'ab;cdefg|hijk\tlmno\np,qrstuv\rwxyz'
# 其中[,、;、|、\t、\n、\r]都是分隔符

# 方法1：连续使用str.split()方法，每次处理一种分隔符号；
# 方法2：使用正则表达式的re.split()方法，一次性拆分。✓
import os
import re
import stat
import string
import unicodedata

s = 'ab;ab|cdefg| |,hijk\tlmno\np,qrstuv\rwxyz'

res = s.split(",")

# lambda 匿名函数
# lambda x（传入的参数）：要执行的语句（这条语句执行完之后，就会返回一个值，也就是函数的返回值）
map(lambda x: x.split('|'), s)

# 方法1：
"""
    input_str：输入字符串
    separator_strs：分隔符列表
"""


def splits(input_str, separator_strs):
    # 将字符串转为列表，格式化
    res = [input_str]
    for d in separator_strs:
        t = []
        # 使用map进行遍历，并使用lambda语法对结果附加操作，extend追加列表
        map(lambda x: t.extend(x.split(d)), res)
        res = t

    # 过滤空字符串
    res = [x for x in res if x]
    # filter(None, res)， None代表不输入函数，也就是[x for x in res if x]
    # res = filter(None, res)
    return res


print(splits(s, [",", ";", "|", "\t", "\n", "\r"]))

# 方法2：
# 使用正则表达式
res = re.split(r'[,;\|\t\n\r]+', s)

print(res)

"""
字符串，开头和结尾
"""

dir = os.listdir(".")
print(dir)

# for name in dir:
#     if name.endswith((".py", ".git")):
#         print(name)
s = [name for name in dir if name.endswith((".py", ".git"))]
print(s)

print(os.stat('json_excel.py'))
# posix.stat_result(st_mode=33252, st_ino=4703033, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=806, st_atime=1592359352, st_mtime=1592298117, st_ctime=1610204877)
print(os.stat('json_excel.py').st_mode)
# 33252
print(oct(os.stat('json_excel.py').st_mode))
# 0100744

# 修改文件权限类型，增加执行权限
os.chmod('json_excel.py', os.stat('json_excel.py').st_mode | stat.S_IXUSR)

"""
    调整文本字符串的格式
    如将日志中的中国时间格式改为美国时间格式
    
    解决方案：
    使用正则表达式re.sub()方法做字符串替换，利用正则表达式的捕捉组，捕捉每部分内容，在替换字符串中调整每个捕捉组的顺序
"""
log = open('logs/log.log').read()
# 示例时间：[2020-05-19 20:58:58,675]
# 其中第二参数表示捕捉组位置，进行调换顺序
# print(re.sub('(\d{4})-(\d{2})-(\d{2})', r"\2/\3/\1", log))
# 除了使用序号还可以使用别名，?P<>定义，\g<>使用
print(re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r"\g<month>/\g<day>/\g<year>", log))

"""
    将多个小字符串拼接成一个大的字符串
    如自定义协议，需要格式化文本
"""
# 协议数据
pl = ["Request Method", "GET",
      "Status Code", "200 OK",
      "Content-Type", "text/plain; charset=UTF-8",
      "Date", "Sun, 10 Jan 2021 13:55:35 GMT",
      "Host", "www.gaox.net",
      "Pragma", "no-cache",
      "Cache-Control", "no-cache",
      "Accept", "application/json, text/javascript, */*; q=0.01",
      "User-Agent",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"]
# 拼接内容
s = ""
# 大量的临时变量，存在资源浪费
for p in pl:
    s += p

print(s)

# string的join方法
s = ''.join(pl)
print(s)
"""
   当列表中包含非字符串内容时 
"""
pl.extend([123])
pl.append(125)
s = ''.join(str(x) for x in pl)
print(s)
"""
    python中的字符串格式化
    str对象的ljust、rjust、center方法的左右居中对齐
    使用format方法，传递类似'<20','>20','^20'参数完成
"""

d = {"id": 10000008,
     "username": "gaoxizhi",
     "name": "Eric",
     "nickname": "Eric",
     "path": "/gaoxizhi",
     "block": False
     }
s = ''
# 求字典d的最大索引长度
w = max(map(len, d.keys()))
# 格式化拼接
for k in d:
    s += "".join([k.ljust(w), ': ', str(d[k]), '\n'])

print(s)

"""
    去掉字符串中不需要的字符
    1、去掉字符串两端空白字符：字符串strip()、lstrip()、rstrip()方法
    2、删除固定位置字符     ：使用切片+拼接方式
    3、删除任意位置字符     ：字符串的replace()方法或正则表达式re.sub()删除
    4、同时删除多种不同字符  ：字符串的translate()方法
"""
s = '----gaox+++'
print(s.strip('-+'))

s = 'name:gaox'
print(s[:4] + s[5:])

s = 'name\tgaox\r\nage\t23\r\n'
print(s)
print(s.replace('\r', '').replace('\t', ''))
print(re.sub('[\r\t]', '', s))
print(s.translate(None, '\r\t'))

"""
    str的translate方法，把一个字符映射到另一个字符，映射和加密逻辑
    如abcd映射为wxyz
"""

s = 'abcgaox'
# wxygwob
print(s.translate(string.maketrans('abcdzyxw', 'wxyzdcba')))

"""
    去掉拼音声调
"""
s = u'gāo shān liú shuǐ'
print(s)
s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
print(s)
