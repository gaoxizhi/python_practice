# !/usr/local/bin/ python
# -*- coding:utf-8 -*-
"""
    让对象支持上下文管理
    实现上下文管理协议，需要定义实例的__enter__，__exit__方法，他们分别在with开始和结束时被调用
"""
from collections import deque
from sys import stdin, stdout
from telnetlib import Telnet

"""
class TelnetClient(object):
    def __init__(self, addr, port=22):
        self.addr = addr
        self.port = port
        self.tn = None

    def start(self):
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()

        # user
        t = self.tn.read_until(('login: '))
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)

        # password
        t = self.tn.read_until('Password: ')
        if t.startswith(user[:-1]): t = t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())

        t = self.tn.read_until('$ ')
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput)
            t = self.tn.read_until('$ ')
            stdout.write(t[len(uinput) + 1:])

    def cleanup(self):
        self.tn.close()
        self.tn = None
        with open(self.addr + '_history.txt', 'w')as f:
            f.writelines(self.history)


client = TelnetClient('gaox.net')
print ('start...')
client.start()
print ('cleanup...')
"""


class TelnetClient(object):
    def __init__(self, addr, port=22):
        self.addr = addr
        self.port = port
        self.tn = None

    def start(self):
        # user
        t = self.tn.read_until(('login: '))
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)

        # password
        t = self.tn.read_until('Password: ')
        if t.startswith(user[:-1]): t = t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())

        t = self.tn.read_until('$ ')
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput)
            t = self.tn.read_until('$ ')
            stdout.write(t[len(uinput) + 1:])

    def cleanup(self):
        pass

    def __enter__(self):
        # 进入对象实例时创建连接
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()
        # 最终返回值
        return self

    # 正常没有异常时：后面三个值都为None
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tn.close()
        self.tn = None
        with open(self.addr + '_history.txt', 'w')as f:
            f.writelines(self.history)
        # python的默认返回值是None，此时返回True，不会向上抛出异常
        return True


client = TelnetClient('gaox.net')
print('start...')
client.start()
print('cleanup...')

with TelnetClient('gaox.net') as client:
    client.start()
