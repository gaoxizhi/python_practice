# -*- encoding=utf-8 -*-
# 导入 random(随机数) 模块
import random
''' 按需生成并“返回”结果，而不是一次性产生所有的返回值
generator使用场景：
　　1. 当我们需要一个公用的，按需生成的数据
　　2. 某个事情执行一部分，另一部分在某个事件发生后再执行下一部分，实现异步。

注意事项：
    1. yield from generator_obj 本质上类似于 for item in generator_obj: yield item
    2. generator函数中允许使用return，但是return 后不允许有返回值
'''


def generator_example():
    yield 1
    yield 2
    # yield 函数会空，类似与迭代器，超过容量后会报 StopIteration 异常


def generators():
    return (random.randint(1, 100) for x in range(1, 9))


e = generator_example()
f = generators()


def getE():
    try:
        # 使用全局变量，可修改外部变量
        global e
        return next(e)
    except StopIteration:
        e = generator_example()
        return next(e)
    else:
        return ("咋回事？")


def getF():
    try:
        # 使用全局变量，可修改外部变量
        global f
        return next(f)
    except StopIteration:
        f = generators()
        return next(f)
    else:
        return ("咋回事？")


for x in range(10):
    print(getE(), getF(), end=' : ')
print(0)
