# 栈的应用: 简单括号匹配

'''
从左到又扫描括号串， 最新打开的左括号， 应该匹配到最后遇到的右括号
'''

from p15 import Stack

def parChecker(symbolString):
    s = Stack()
    index = 0
    balanced = True
    while index < len(symbolString):
        symbol = symbolString[index]
        #if symbol == "(":
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False

        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

# print(parChecker('((()))'))
# print(parChecker('(()'))

'''matches小技巧'''
def matches(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)

print(parChecker('{{([][]}()}'))
print(parChecker('[{()]'))