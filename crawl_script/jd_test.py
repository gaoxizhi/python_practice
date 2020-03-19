#-*-encoding=utf-8-*-

import requests, time, ssl, os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.error import URLError

# 全局取消证书验证
# 异常----> SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://list.jd.com/list.html?cat=9987,653,655"

res = requests.get(url)
# print(res.text)

# 使用BeautifulSoup解析数据
soup = BeautifulSoup(res.text, "lxml")

#  获取图片信息
img_list = soup.find_all(name="img", attrs={'width': '220', 'height': '220'})
print("本页中商品数量：", len(img_list))

# 遍历
m = 0
# 判断或创建文件夹
if not os.path.exists("./mypic/"):
    if not os.path.isdir("./mypic/"):
        os.mkdir("./mypic/")

for img in img_list:
    m += 1
    # 判断当前图拍呢的属性是否有src，并获取图片上的url地址
    if "src" in img.attrs:
        img_url = "https:" + img.attrs['src']
    else:
        # 京东使用类似懒加载的方式
        img_url = "https:" + img.attrs['data-lazy-img']
    img_file = ("./mypic/p" + str(m) + ".jpg")

    # 拦截超时，并重试机制
    count = 1
    while count <= 5:
        try:
            urlretrieve(url, img_file)
            break
        except URLError:
            err_info = 'Reloading for %d time' % count
            print(err_info)
            count += 1
    if count > 5:
        print("download job failed!")
    
    # 另一种实现方式
    '''
    with requests.get(img_url, stream=True) as ir:
        with open(img_file, "wb") as f:
            for chunk in ir:
                f.write(chunk)
    '''
    print(img_file)
