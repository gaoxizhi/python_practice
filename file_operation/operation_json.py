# !/usr/local/bin/ python3
# -*- coding:utf-8 -*-

"""
    使用标准库中的json模块，其中loads、dumps函数可以完成json数据的读写

    json.dump()将json内容写入到文件
    json.load()将文件内容载入为json
"""

import json

l = [1, 2, 'abc', {"name": "gaox", "age": 23, "maritalStatus": None}]

# None对应null
# [1, 2, "abc", {"age": 23, "maritalStatus": null, "name": "gaox"}]
d = json.dumps(l)
print(d)
# json的不同分隔符
ds = json.dumps(l, separators=[',', ':'])
print(ds)

d = {"name": "gaox", "age": 23, "maritalStatus": None}
print(json.dumps(d, sort_keys=True))
# python2 校验不严格
# l2 = json.loads(ds)
# print(l2)
# print(l2[0])

