# -*- encoding=utf-8 -*-

# 创建一个空列表
member = []
print(member)

# 创建并初始化列表
member = ['高羲之', '习近平', '马云']
print(member)

# 一个元素在末尾追加
member.append('慕容复')
print(member)

# 传入参数过多，应使用
# member.append("东华帝君","张果老")

# 在末尾添加多个元素
member.extend(["东华帝君", "张果老"])
print(member)

# 添加指定位置元素，位置以后的元素后移
print('member.insert(0,"牡丹"): ', member.insert(0, "牡丹"))
print(member)
# ------------------------------------
'''删除元素 三种方式'''

# 必须使用字段，不能使用索引
member.remove('习近平')
print(member)

# 出栈最后一个
print('member.pop(): ', member.pop())

# 删除指定元素
del (member[0])
print(member)
# --------------------------------------

# 列表切片:
# [:3] 分片出3个元素（拷贝）
# [2:] 从第3个开始
print('member[2:]: ', member[2:])

# -------------------------------------
# 验证列表含有元素
print("\"习近平\" not in member:", "习近平" not in member)
print("\"习近平\" in member:", "习近平" in member)

# -------------------------------------
# 寻找索引位置
print('''member.index('高羲之'): ''', member.index('高羲之'))
# 列表方法
'''
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', 
'__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
'remove', 'reverse', 'sort']

'''
