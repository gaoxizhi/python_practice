# !/usr/local/bin/ python3
# -*- coding:utf-8 -*-
"""
    分析程序内那些函数执行时间开销较大

    定义一个带timeout参数的函数装饰器
    1. 统计被装饰器函数单次调用运行时间
    2. 时间大于timeout的将此函数调用记录到log日志中
    3. 运行时可修改timeout的值

    为包裹函数增添一个函数，用来修改闭包中使用的自由变量
    在python3中使用nonlocal访问嵌套作用域中的变量引用
"""
import logging
import time
from random import randint


def warn(timeout):
    timeout = [timeout]

    def decorator(func):
        def wrapper(*args, **kargs):
            start = time.time()
            res = func(*args, **kargs)
            used = time.time() - start
            if used > timeout[0]:
                msg = '"%s": %s > %s' % (func.__name__, used, timeout[0])
                logging.warning(msg)
            return res

        def set_timeout(k):
            # nonlocal timeout
            timeout[0] = k

        wrapper.setTimeout = set_timeout
        return wrapper

    return decorator


@warn(1.5)
def test():
    print('In test')
    while randint(0, 1):
        time.sleep(0.5)


for _ in range(30):
    test()

test.setTimeout(1)
for _ in range(30):
    test()
