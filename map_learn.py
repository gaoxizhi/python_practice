# -*- encoding=utf-8 -*-

dii = dict({"a": 10, "b": 21})
print(dii)
for i in range(1, 10):
    print('now number is %d' % i)
    for j in (1, 2):
        print('has number %s' % (str(i) + str(j)))
