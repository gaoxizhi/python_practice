# -*- coding: utf-8 -*-
import oss2
import time


def CalculateFolderLength(bucket, folder):
    length = 0
    for obj in oss2.ObjectIterator(bucket, prefix=folder):
        length += obj.size
    return length


host = "http://oss-cn-beijing.aliyuncs.com"
accessid = "accessid"
accesskey = "accesskey"
bucket_name = "gaox-av"

auth = oss2.Auth(accessid, accesskey)
bucket = oss2.Bucket(auth, host, bucket_name)
'''
# 列举leek文件夹下的文件与子文件夹名称，不列举子文件夹下的文件。
for obj in oss2.ObjectIterator(bucket, prefix='leek/', delimiter='/'):
    # 通过is_prefix方法判断obj是否为文件夹。
    if obj.is_prefix():  # 文件夹
        length = CalculateFolderLength(bucket, obj.key)
        print('directory: ' + obj.key + '  length:' + str(length) + "Byte.")
    else:  # 文件
        print('file: ' + obj.key + '  length:' + str(obj.size) + "Byte.")
'''


def dt2str(x):
    time_local = time.localtime(x)
    dt = time.strftime("%Y年%m月%d日 %H:%M:%S", time_local)
    return dt


def str2dt(dt):
    # 转为时间数组
    try:
        timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    except:
        timeArray = time.strptime(time.localtime(0))

    # 转为时间戳
    return int(time.mktime(timeArray))


def print_all_file_info(prefix_dir):
    # 列举prefix_dir文件夹下的文件与子文件夹名称，不列举子文件夹下的文件。
    for obj in oss2.ObjectIterator(bucket, prefix=prefix_dir, delimiter='/'):
        # 通过is_prefix方法判断obj是否为文件夹。
        if obj.is_prefix():  # 递归文件夹
            print_all_file_info(str(obj.key))
        else:  # 文件
            print('file: ' + obj.key + '  length:' + str(obj.size) +
                  "Byte  last_modified:" + dt2str(obj.last_modified))


print_all_file_info("leek/")
print(str2dt("2020-03-23 10:59:59"))
