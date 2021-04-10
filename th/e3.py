# !/usr/local/bin/ python
# -*- coding:utf-8 -*-

"""
    自定义行为：过滤小于0的数据

    功能：派生内置不可变类型并修改其实例化行为
    逻辑：定义IntTuple继承内置tuple，并实现__new__修改实例化行为
"""


class IntTuple(tuple):
    # python的构造区

    def __new__(cls, iterable):
        # 完成参数的过滤和修改
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        # 调用父类构造器
        return super(IntTuple, cls).__new__(cls, g)

    # 在此处已经构造完成
    def __init__(self, iterable):
        super(IntTuple, self).__init__(iterable)


t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
print(t)
