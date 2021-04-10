# !/usr/local/bin/ python
# -*- coding:utf-8 -*-
"""
    由于全局解释器锁的存在，多线程进行CPU密集型擦欧总并不能提高执行效率

    如何提升多种操作组合的程序执行效率
    1、使用多个多个IO操作
    2、使用一个ConvertThread线程进行转换（CPU密集型操作）
    3、IO操作线程将数据安全的传递给转换线程

    多线程通讯
    使用标准库中Queue.Queue线程安全的队列

    线程间事件通知
    可以使用标准库中Threading.event
    1. 等待事件一端调用wait，等待事件，线程进入睡眠状态，直到对端调用set函数
    2. 通知事件一端调用set，通知事件

    线程的本地数据
    threading.local函数可以创建线程本地数据空间，其下属性对每个线程独立存在

    线程池

    使用标准库中concurrent.futures下的ThreadPoolExecutor对象
    的submit和map方法可以用来启动线程池中线程执行任务
"""

import os
import tarfile
import threading
from concurrent.futures import ThreadPoolExecutor


def tarXML(tfname):
    tf = tarfile.open(tfname, 'w:gz')
    for fname in os.listdir('.'):
        if fname.endswith('.xml'):
            tf.add(fname)
            # 删掉该文件
            os.remove(fname)
    tf.close()


l = threading.local()
l.x = 1


def f():
    print(l.x)


f()

executor = ThreadPoolExecutor(3)


def f(a, b):
    print('f', a, b)
    return a ** b


future = executor.submit(f, 5, 3)

print(future.result())

ex = executor.map(f, [2, 3, 5], [2, 5, 3])
