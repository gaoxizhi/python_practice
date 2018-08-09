size = 3 # 定义菱形尺寸
count = size*2+1 # 定义X,Y坐标循环范围
# i为横坐标
for i in range(count):
    # j为纵坐标
    for j in range(count): 
        # 当X,Y满足条件1和2时
        if i <= size and (j == size-i or j == size+i):
            print('*', end='')
        # 当X,Y满足条件3和4时
        elif i > size and (j == i-size or j == size*3-i):
            print('*', end='')
        # 其它情况输入空格
        else:
            print(' ', end='')
    # 每打印一行就换行
    print()
