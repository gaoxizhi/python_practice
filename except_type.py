# -*- encoding=utf-8 -*-

size = ''
while (not (isinstance(size, int))):
    try:
        # eval 自动类型转换
        size = eval(size)
    # 这里不指定类型，全部处理
    except:
        size = input("请输入菱形的尺寸：\n")

size = eval(str(size))
count = size * 2 + 1  # 定义X,Y坐标循环范围
# i为横坐标
for i in range(count):
    # j为纵坐标
    for j in range(count):
        # 当X,Y满足条件1和2时
        if i <= size and (j == size - i or j == size + i):
            print('*', end='')
        # 当X,Y满足条件3和4时
        elif i > size and (j == i - size or j == size * 3 - i):
            print('*', end='')
        # 其它情况输入空格
        else:
            print(' ', end='')
    # 每打印一行就换行
    print()
