# 四个生成前n个整数列表的方法

def test1():
    l = []
    for i in range(1000):
        l = l + i
def test2():
    l = []
    for i in range(1000):
        l.append(i)
def test3():
    l = [i for i in range(1000)] # python中的解析式 https://zhuanlan.zhihu.com/p/79685561

def test4():
    l = list(range(1000))
