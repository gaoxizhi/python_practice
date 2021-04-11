# -*-encoding=utf-8-*-

import os
import shutil

from pyquery import PyQuery

"""
    适配 拉勾网-拉勾教育 网页保存
        效果：图片文件统一保存到img文件夹下
        
    遍历文件夹
    1、删除css、js文件
    2、将其他文件（主要是图片）移动到上层目录
    3、使用pyquery处理文本，只抓取指定内容
    4、转成文本，将图片、图标资源路径做修改
    5、将处理后的文本存储文件
    6、移除空目录
"""


def main():
    # 设置父目录
    dir_path = "/Users/gaox/Downloads/new"
    dir = os.listdir(dir_path)
    # 遍历父目录，以其子项为最小单元
    for i in dir:
        # 子目录处理
        sub_dir_path = os.path.join(dir_path, i)
        if os.path.isdir(sub_dir_path):
            print("正在处理课程【%s】..." % sub_dir_path)

            for j in os.listdir(sub_dir_path):
                # 新建图片资源目录
                img_path = os.path.join(sub_dir_path, "img")
                if not os.path.exists(img_path):
                    os.mkdir(img_path)

                chapter_path = os.path.join(sub_dir_path, j)

                if os.path.isdir(chapter_path):
                    print("正在处理章节【%s】..." % chapter_path)

                    for k in os.listdir(chapter_path):
                        file_path = os.path.join(chapter_path, k)
                        # 2、进入其子目录将图片资源移动到img_path，已存在则不处理
                        if file_path.endswith(".png") or file_path.endswith(".jpg") or file_path.endswith("jpeg") \
                                or file_path.endswith("bmp") or file_path.endswith("gif"):
                            if not os.path.exists(os.path.join(img_path, k)):
                                shutil.move(file_path, img_path)

                    # 清理文件夹包含css、js等文件，不包含img文件夹
                    if not j == "img":
                        for k in os.listdir(chapter_path):
                            file_path = os.path.join(chapter_path, k)
                            print("清理文件【%s】..." % file_path)
                            os.remove(file_path)

                # 处理html中资源路径
                if chapter_path.endswith(".html"):
                    get_pure_text(chapter_path, img_path)

                # 移除资源目录
                if os.path.isdir(chapter_path) and not j == "img":
                    os.removedirs(chapter_path)


# 3、使用pyquery处理文本，只抓取指定内容
def get_pure_text(file_path, img_path):
    f = open(file_path, "r", encoding="utf-8")
    content = f.read()
    f.close()

    # 使用pyquery解析网页
    doc = PyQuery(content)

    # 获取正文
    text = doc(".right-content-wrap")
    # 移除音频媒体
    text(".media-player-wrap").remove()
    if not text:
        # 如果已经处理或者没有指定节点则跳过
        text = doc

    # 处理图片资源路径
    for i in text.items('img'):
        src = i.attr('src')
        # 图片资源路径空
        if not None == src:
            if src.endswith(".png") or src.endswith(".jpg") or file_path.endswith("jpeg") \
                    or file_path.endswith("bmp") or file_path.endswith("gif"):
                local_img_dir_path = img_path.split("/")[-1]
                # 本地图片 设置新路径
                if src.startswith("./"):
                    split_path = src.split("/")
                    split_path[1] = local_img_dir_path
                    src_new = "/".join(split_path)
                    i.attr("src", src_new)

                # 网络图片 指向本地图片
                if src.startswith("http"):
                    split_path = src.split("/")
                    split_path[1] = local_img_dir_path
                    file_name = split_path[-1]

                    src_new = os.path.join(os.path.join("./", local_img_dir_path), file_name)
                    src_in_img = os.path.join(img_path, file_name)
                    # 判断本地文件是否包含
                    if os.path.exists(src_in_img):
                        i.attr("src", src_new)

    # svg 图片 清理点赞图标 class="message-list-title-right"
    text(".message-list-title-right").remove()
    # 去除乱七八糟标签
    # 或者只保留：href、src、alt、style
    label = ["p", "code", "li", "ul", "strong", "div", "img", "h2", "h3", "h4", "span", "a"]
    for key in label:
        for i in text.items(key):
            i.remove_attr("class")
            i.remove_attr("data-nodeid")

    # 设置正文class属性，保证脚本可重新执行
    text.attr("class", "right-content-wrap")

    # 拼接完整html文件
    html = """<!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    </head>
    <body>
    """ + str(text) + """
    </body>
    </html>
    """

    f = open(file_path, "w", encoding="utf-8")
    f.write(html)
    f.close()


if __name__ == "__main__":
    main()
