# !/usr/local/bin/ python
# -*- coding:utf-8 -*-
"""
    使用第三方库xlrd和xlwt，这两个库分别用于excel的读和写
"""
import xlrd

book = xlrd.open_workbook('../files/receipt.xlsx')
# 获取excel有多少个sheet
print(list(book.sheet_names()))
sheet = book.sheets()[0]
# 获取总行数
nrows = sheet.nrows
print(nrows)
# 获取总列数
ncols = sheet.ncols
print(ncols)

# 获取一行的数值
print(sheet.row_values(0))
# 获取一列的数值
key = sheet.col_values(0)
colors = sheet.col_values(1)
print(key)

for x in range(4, nrows):
    print(''.join([key[x], '款', colors[x], '色']))

