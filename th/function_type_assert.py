# !/usr/local/bin/ python3
# -*- coding:utf-8 -*-
"""
    函数修饰器，规定参数类型
"""
from inspect import signature


def type_assert(*ty_args, **ty_kargs):
    def decorator(func):
        # fun -> a,b
        # d = ('a':int, 'b':str)
        sig = signature(func)
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments

        def wrapper(*args, **kargs):
            # arg in d, instance(arg,d[arg])
            for name, obj in sig.bind_partial(*args, **kargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('"%s" must be "%s"' % (name, btypes[name].__name__))
            return func(*args, **kargs)

        return wrapper

    return decorator


@type_assert(int, str, list)
def f(a, b, c):
    print('args is %s(%s), %s(%s), %s(%s).' % (str(a), type(a), b, type(b), str(c), type(c)))


f(1, 'ga', [1, 2, 5])
f(7, 'gaoxizhi', [1, 2, 3])
f(1, 'ga', "1")
