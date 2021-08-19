# 四个生成前n个整数列表的方法

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)] # python中的解析式 https://zhuanlan.zhihu.com/p/79685561

def test4():
    l = list(range(1000))

from timeit import Timer
t1 = Timer("test1()", "from __main__ import test1")
print("concat {} seconds".format(t1.timeit(number=1000)))

t2 = Timer("test2()", "from __main__ import test2")
print("append {} seconds".format(t2.timeit(number=1000)))

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension {} seconds".format(t3.timeit(number=1000)))

t4 = Timer("test4()", "from __main__ import test4")
print("list range {} seconds".format(t4.timeit(number=1000)))