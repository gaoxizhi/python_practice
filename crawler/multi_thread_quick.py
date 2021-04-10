#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
import urllib.request
import re
import urllib.error
for i in range(1,10):
    pageurl="http://www.58pic.com/haibaomoban/0/id-"+str(i)+".html"
    data=urllib.request.urlopen(pageurl).read().decode("utf-8","ignore")
    pat='<a class="thumb-box".*?src="(.*?).jpg!'
    imglist=re.compile(pat).findall(data)
    for j in range(0,len(imglist)):
        try:
            thisimg=imglist[j]
            thisimgurl=thisimg+"_1024.jpg"
            file="/Users/gaox/codeing/py/"+str(i)+str(j)+".jpg"
            urllib.request.urlretrieve(thisimgurl,filename=file)
            print("第"+str(i)+"页第"+str(j)+"个图片爬取成功")
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
            if hasattr(e,"reason"):
                print(e.reason)
        except Exception as e:
            print(e)
'''
'''
import urllib.request
import re
import urllib.error
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
comid="6165793094371986503"
url="http://video.coral.qq.com/filmreviewr/c/upcomment/0dfpyvfa7tp0ewe?commentid="+comid+"&reqnum=3&callback=jQuery1120026430801920245595_1478436999932&_=1478436999935"
for i in range(0,100):
    data=urllib.request.urlopen(url).read().decode()
    patnext='"last":"(.*?)"'
    nextid=re.compile(patnext).findall(data)[0]
    patcom='"content":"(.*?)",'
    comdata=re.compile(patcom).findall(data)
    for j in range(0,len(comdata)):
        print("------第"+str(i)+str(j)+"条评论内容是:")
        print(eval('u"'+comdata[j]+'"'))
    url="http://video.coral.qq.com/filmreviewr/c/upcomment/0dfpyvfa7tp0ewe?commentid="+nextid+"&reqnum=3&callback=jQuery1120026430801920245595_1478436999932&_=1478436999935"
'''

'''
import urllib.request
import re
import urllib.error
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(1,36):
    url="http://www.qiushibaike.com/8hr/page/"+str(i)
    pagedata=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
    datalist=re.compile(pat,re.S).findall(pagedata)
    for j in range(0,len(datalist)):
        print("第"+str(i)+"页第"+str(j)+"个段子的内容是：")
        print(datalist[j])
'''
'''
import threading
class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0,10):
            print("我是线程A")
class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0,10):
            print("我是线程B")
t1=A()
t1.start()
t2=B()
t2.start()
'''
import re
import threading
import urllib.error
import urllib.request

headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)


class One(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(1, 36, 2):
            # https://www.qiushibaike.com/8hr/page/2/
            url = "https://www.qiushibaike.com/8hr/page/" + str(i)
            page_data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
            pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
            datalist = re.compile(pat, re.S).findall(page_data)
            for j in range(0, len(datalist)):
                print("第" + str(i) + "页第" + str(j) + "个段子的内容是：")
                print(datalist[j])


class Two(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(0, 36, 2):
            url = "http://www.qiushibaike.com/8hr/page/" + str(i)
            page_data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
            pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
            datalist = re.compile(pat, re.S).findall(page_data)
            for j in range(0, len(datalist)):
                print("第" + str(i) + "页第" + str(j) + "个段子的内容是：")
                print(datalist[j])


one = One()
one.start()
two = Two()
two.start()
