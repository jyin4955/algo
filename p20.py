# 后缀表达式求值

from p15 import Stack
from p18 import infixTOPostfix
def calPosfix(postfixExpr):
    operandStack = Stack()
    lst = postfixExpr.split(" ")
    i = 0
    while i < len(lst):
        token = lst[i]
        #print(token)
        if token in '0123456789':
            operandStack.push(int(token))
        elif token in '*/+-':
            right = operandStack.pop()
            left = operandStack.pop()
            res = doMath(token, left, right)
            operandStack.push(res)
        i += 1
    return operandStack.pop()

def doMath(operator, left, right):
    if operator == '*':
        return left * right
    elif operator == '/':
        return left / right
    elif operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    # 只能做十位以内加减乘除法
# print('10' in '0123456789') >> False
if __name__ == '__main__':
    postfixExpr = infixTOPostfix('5 + 6 - ( 8 / 4 )')
    print(postfixExpr)
    print(calPosfix(postfixExpr))

    postfixExpr = infixTOPostfix('3 + 4 - ( 8 / 4 )')
    print(postfixExpr)
    print(calPosfix(postfixExpr))