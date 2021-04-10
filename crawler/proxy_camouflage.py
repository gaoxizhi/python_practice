#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
import re
import urllib.request

data = urllib.request.urlopen("http://news.sina.com.cn/").read()
data2 = data.decode("utf-8", "ignore")
pat = 'href="(http://news.sina.com.cn/.*?)"'
allurl = re.compile(pat).findall(data2)
for i in range(0, len(allurl)):
    try:
        print("第" + str(i) + "次爬取")
        thisurl = allurl[i]
        file = "/Users/gaox/codeing/py/" + str(i) + ".html"
        urllib.request.urlretrieve(thisurl, file)
        print("-------成功-------")
    except urllib.error.URLError  as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

'''

'''
import urllib.request
import re

url = "http://blog.csdn.net/"
headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
pat = '<h3  class="tracking-ad" data-mod="popu_254"><a href="(.*?)"'
result = re.compile(pat).findall(data)
for i in range(len(result)):
    file = "/Users/gaox/codeing/py/" + str(i) + ".html"
    urllib.request.urlretrieve(result[i], filename=file)
    print("第" + str(i + 1) + "次爬取成功")
'''

'''
""" 
    使用代理IP
"""
import urllib.request
def use_proxy(url, proxy_addr):
    proxy = urllib.request.ProxyHandler({"http": proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    return data

proxy_addr = ["119.183.220.224:8888", ""]
url = "http://www.baidu.com"
data = use_proxy(url, proxy_addr)
print(len(data))
'''

import re
import urllib.request

keyname = "连衣裙"
key = urllib.request.quote(keyname)
headers = ("User-Agent",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
for i in range(1, 10):
    url = "https://s.taobao.com/list?q=" + key + "&cat=16&style=grid&seller_type=taobao&spm=a219r.lm874.1000187.1&bcoffset=12&s=" + str(
        i * 60)

    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    pat = 'pic_url":"//(.*?)"'
    imagelist = re.compile(pat).findall(data)
    for j in range(len(imagelist)):
        thisimg = imagelist[j]
        thisimgurl = "http://" + thisimg
        file = "/Users/gaox/codeing/py/" + str(i) + str(j) + ".jpg"
        urllib.request.urlretrieve(thisimgurl, filename=file)
