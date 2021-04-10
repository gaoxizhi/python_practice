# !/usr/local/bin/ python
# -*- coding:utf-8 -*-

"""
    声明实例属性名称的列表，在海量实例中节省内存空间

    实例的__dict__，实现了属性动态绑定的特性，是以牺牲内存为代价而带来的功能
    用__slots__声明实例属性列表，类似于C语言中的结构体，来阻止动态属性绑定，进而节省空间
"""
import sys


class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level


class Player2(object):
    __slots__ = ['uid', 'name', 'stat', 'level']

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


p1 = Player('001', 'gaox')
p2 = Player2('002', 'gaox')

"""
    p1比p2多了属性：__dict__, status, __weakref__
    __weakref__ ：弱引用
"""
print(set(dir(p1)) - set(dir(p2)))

print(p1.__dict__)
# 可以动态向对象字典绑定属性内容
p1.__dict__['y'] = 97

# 解除属性，删除属性y
del p1.__dict__['y']

print(sys.getsizeof(p1))
print(sys.getsizeof(p2))
