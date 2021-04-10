# !/usr/local/bin/ python
# -*- coding:utf-8 -*-
from abc import abstractmethod
from math import pi

"""
    比较运算符号重载，需要实现以下方法：
    __lt__, __le__, __gt__, __ge__, __eq__, __ne__
    使用标准库下的functools下的类装饰器total_ordering可以简化此过程
    只需定义__eq__和__lt__, __le__中任意一个方法，其余都可以通过组合进行实现
"""

from functools import total_ordering


@total_ordering
class Shape(object):

    # 定义抽象方法：定义为空（pass）
    @abstractmethod
    def area(self):
        pass

    def __lt__(self, obj):
        print('__lt__')
        if not isinstance(obj, Shape):
            raise TypeError('The incoming object is not of Shape type.')
        return self.area() < obj.area()

    def __eq__(self, obj):
        print('__eq__')
        if not isinstance(obj, Shape):
            raise TypeError('The incoming object is not of Shape type.')
        return self.area() == obj.area()


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, radius):
        self.__set__(self, radius)
        # self.radius = radius

    def __get__(self, instance, owner):
        return instance.__dict__[self.radius]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError('wrong type. must be in int, long, float!')
        instance.__dict__['radius'] = value

    def area(self):
        return self.radius ** 2 + pi


c1 = Circle(12)
r1 = Rectangle(5, 21)
print(''.join(['c1=[', str(c1.area()), '], r1=[', str(r1.area()), ']']))
print(c1 > r1)
print(r1 > c1)
