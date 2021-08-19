# list.pop 计时实验
import timeit
popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("y.pop()", "from __main__ import y")

x = list(range(2000000))
print(popzero.timeit(number=1000))

y = list(range(2000000))
print(popend.timeit(number=1000))

## 设计一个性能试验来验证list中检索一个值， 以及dict中检索一个值的计时对比
# 生成包含连续值的list和包含连续关键码key的dict，用随机数来检验操作符in的耗时
import timeit
import random
for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange({}) in x".format(i), "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)} # key 对应的value值为none
    d_time = t.timeit(number=1000)
    print("{}, {:.3f}, {:.3f}".format(i, lst_time, d_time))

