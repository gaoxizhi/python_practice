# !/usr/local/bin/ python
# -*- coding:utf-8 -*-
from functools import update_wrapper

"""
    如何为被装饰的函数保存元数据

    在函数对象中保存着一些函数的元数据，例如：
    f.__name__     ：函数的名字
    f.__doc__      ：函数文档
    f.__module__   ：函数所属模块名
    f.__dict__     ：函数字典
    f.__defaults__ ：函数默认参数元组
    ...
    使用装饰器再使用上面这些属性访问时，看到的内部包裹函数的元数据，原来函数的元数据便丢失掉了

    使用标准库functools中的装饰器wraps装饰内部包裹函数，可以制定将原函数的某些属性，更新到包裹函数上面。
"""


def f(a):
    """f function"""
    return a * 2


# 'f'
print(f.__name__)

g = f
# 'f' 函数名称是在定义（def）时确定的
print(g.__name__)


def my_decorator(func):
    def wrapper(*args, **kargs):
        print('In wrapper')
        func(*args, **kargs)
        # update_wrapper(wrapper, func, ('__name__', '__doc__'), ('__dict__',))
        update_wrapper(wrapper, func)
        return wrapper


@my_decorator
def example():
    """example function"""
    print('In example')


# print (WRAPPER_ASSIGNMENTS)
# print (WRAPPER_UPDATES)
# print (example.__name__)
# print (example.__doc__)


from inspect import signature


def type_assert(*ty_args, **ty_kargs):
    def decorator(func):
        # fun -> a,b
        # d = ('a':int, 'b':str)
        sig = signature(func)

        def wrapper(*args, **kargs):
            return func(*args, **kargs)

        return wrapper

    return decorator
