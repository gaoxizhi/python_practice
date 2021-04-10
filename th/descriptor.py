# !/usr/local/bin/ python
# -*- coding:utf-8 -*-

"""
    使用描述符对实例属性做类型检查
    使用描述符来实现需要类型检查的属性，分别实现：__get__, __set__, __delete__方法，
    在__set__内使用insistence函数做类型检查。
"""
import sys
import weakref


class Attr(object):
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError('expected an %s' % self.type_)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Person(object):
    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)


p = Person()
p.name = 'gaox'
print(p.name)
# p.age = '23'
p.age = 23
print(p.age)

"""
    在python中，垃圾回收器通过计数来回收垃圾对象，但某些环状数据结构（树、图…），存在对象间的循环引用，
    比如树的父节点引用子节点，子节点也同时引用父节点，此时同时del引用父子节点，两个对象不能被立即回收

    使用标准库weakref，他可以创建一种能访问对象但不增加引用计数的对象
"""


class A(object):
    def __del__(self):
        print('in A.__del__')


a = A()
# 2
# return the reference count of object. The conut returned is generally one higher
# than you might expect, because it includes the (temporary)
sys.getrefcount(a)

a2 = a
# 3
sys.getrefcount(a)

del a2
# 2
sys.getrefcount(a)


class Data(object):
    def __init__(self, value, owner):
        self.owner = owner
        self.value = value

    def __str__(self):
        return "%s's data, value is %s" % (self.owner, self.value)

    """
        改写为之后形式后，当调用del方法时，对象就会被立即回收
    """

    # def __init__(self, value, owner):
    #     self.owner = weakref.ref(owner)
    #     self.value = value
    #
    # def __str__(self):
    #     return "%s's data, value is %s" % (self.owner(), self.value)

    def __del__(self):
        print("in Data.__del__")


class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)

    def __del__(self):
        print("in Node.__del__")


node = Node(100)

# 并不会立即回收，所以不会打印出__del__消息
del node
# raw_input('wait...')

# 即使强制回收也不会立即生效
# import gc
# gc.collect()
# raw_input('wait...')


# 弱引用
node = Node(100)
wref = weakref.ref(node)
node2 = wref()

# True
print(node2 is node)

del node
# 此时会打印Node.__del__内信息，此时已被回收
# 并且此时wref对象已经是None了
del node2
