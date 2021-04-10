#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# import pcap, dpkt
# import re, threading, requests

import pcap
# eth0 网卡名称
pc = pcap.pcap('eth0')
pc.setfilter('tcp prot 80')
# ptime 收到的时间，pdata收到的数据
for ptime,pdata in pc:
    print(ptime,pdata)