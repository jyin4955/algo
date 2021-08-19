# 十进制转化为二进制
'''除以2的过程, 得到的余数是从低到高的次序, 而输出则是从高到低的次序, 需要一个栈来反转'''
from p15 import Stack

def devideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2 # 整数除

    binString = ''
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(devideBy2(42))

## 拓展到更多的进制
'''十进制转换到16进制'''

def baseConverter(decNumber,base):
    digits = '0123456789ABCDEF'
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    base_string = ''
    while not remstack.isEmpty():
        base_string = base_string + digits[remstack.pop()]
    return base_string

print(baseConverter(25,2))
print(baseConverter(25,16))