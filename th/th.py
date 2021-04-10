# !/usr/local/bin/ python
# -*- coding:utf-8 -*-
"""
    使用标准库threading.Thread创建线程，在每一个线程中分别执行任务

    python不适合CPU密集型活动，适合IO密集型操作
    在python中有一个全局解释器锁（global interpreter lock）当前只能有一个线程被执行
"""
from threading import Thread


def handle(sid):
    print('Download....(%d)' % sid)


# t = Thread(target=handle, args=(1,))
# t.start()

class MyThread(Thread):
    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid

    def run(self):
        handle(self.sid)


# t = MyThread(1)
# t.start()
# # 阻塞函数，当子线程退出之后才退出
# t.join()

threads = []
for i in range(1, 11):
    t = MyThread(i)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print('main thead was done.')
