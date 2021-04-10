# !/usr/local/bin/ python
# -*- coding:utf-8 -*-
from functools import total_ordering
from math import pi

"""
    类参数校验
"""


class Circle(object):
    def __init__(self, radius):
        # self.radius = radius
        self.setRadius(radius)

    def getRadius(self):
        return self.radius

    def setRadius(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('wrong type.')
        print(value)
        self.radius = float(value)

    def getArea(self):
        return self.radius ** 2 + pi

    # 控制属性访问方法
    # 使用property函数为类创建可管理属性，fget、fset、fdel对应的响应属性访问
    R = property(getRadius, setRadius)


@total_ordering
class Rect(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __lt__(self, obj):
        print('__lt__')
        return self.area() < obj.area()

    def __eq__(self, obj):
        print('__eq__')
        return self.area() == obj.area()


r1 = Rect(5, 3)
r2 = Rect(5, 3)
r3 = Rect(5, 2)

print(r1 <= r2)
print(r2 == r3)

c = Circle(2.1)
c.setRadius('ac')
c.R = '2.g'
print(c.getArea())
