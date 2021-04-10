# !/usr/local/bin/ python3
# -*- coding:utf-8 -*-

import csv

# 以二进制文件方式打开
rf = open('../files/data.csv', 'rb')
reader = csv.reader(rf)
s = reader.next()
s = reader.next()
s = reader.next()
print(s)

wf = open('../files/rong.csv', 'wb')
# wf.truncate(0)
writer = csv.writer(wf)
writer.writerow(['ClassInfo', 'ClassName', 'UserName', 'UserID', 'Article'])

writer.writerow(reader.next())
writer.writerow(reader.next())
writer.writerow(reader.next())
writer.writerow(reader.next())

wf.flush()
rf.close()
wf.close()

with open('../files/data.csv', 'rb') as rf:
    reader = csv.reader(rf)
    with open('../files/yi.csv', 'wb')as wf:
        writer = csv.writer(wf)
        reader.next()
        reader.next()
        headers = reader.next()
        writer.writerow(headers)
        for row in reader:
            if (row[1] < '01/01/2019 00:00:00'):
                break
            weight = row[3].replace('k', '').replace('g', '').strip()
            if (float(weight) != 0):
                writer.writerow(row)
print('end')
