#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import subprocess

import tablib

# json.text文件的格式： [{"a":1},{"a":2},{"a":3},{"a":4},{"a":5}]
# 获取json数据
with open('json.json', 'r') as f:
    rows = json.load(f)

# 将json中的key作为header, 也可以自定义header（列名）
header = tuple([i for i in rows[0].keys()])

data = []
# 循环里面的字典，将value作为数据写入进去
for row in rows:
    body = []
    for v in row.values():
        body.append(v)
    data.append(tuple(body))

data = tablib.Dataset(*data, headers=header)
file_name = 'data.xls'
with open(file_name, 'wb') as f:
    # TypeError: a bytes-like object is required, not 'Dataset'
    f.write(data)
    f.close()
# 使用系统默认应用打开文件
subprocess.call(["open", file_name])
