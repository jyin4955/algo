# 表达式转换　operator 操作符，　operand操作数
# 例如中缀表达式 A + B
# 前缀表达式 +AB
# 后缀表达式 AB＋
# 前缀，　中缀　和后缀表达式https://www.cnblogs.com/zzliu/p/10801113.html
'''
总结下，在从左到右扫描逐个字符扫描中缀表达式的过程中，采用一个栈来暂存未处理的操作符
❖这样，栈顶的操作符就是最近暂存进去的，当遇到一个新的操作符，就需要跟栈顶的操作符比较下优先级，再行处理。
❖后面的算法描述中，约定中缀表达式是由空格隔开的一系列单词（token）构成，操作符单词包括*/+-()而操作数单词则是单字母标识符A、B、C等。
❖首先，创建空栈opstack用于暂存操作符，空表postfixList用于保存后缀表达式
❖将中缀表达式转换为单词（token）列表从左到右扫描中缀表达式单词列表如果单词是操作数，则直接添加到后缀表达式列表的末尾,
如果单词是左括号“(”，则压入opstack栈顶
如果单词是右括号“)”，则反复弹出opstack栈顶
操作符，加入到输出列表末尾，直到碰到左括号
如果单词是操作符“*/+-”，则压入opstack栈顶
• 但在压入之前，要比较其与栈顶操作符的优先级
• 如果栈顶的高于或等于它，就要反复弹出栈顶操作符
，加入到输出列表末尾
• 直到栈顶的操作符优先级低于它
'''

from p15 import Stack
def infixTOPostfix(infixexpr):
    # 记录操作符优先级
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1 # 为什么左括号的优先级为1?
    opstack = Stack()
    postfixList = []
    #tokenList = infixexpr.split()
    i = 0
    while i < len(infixexpr):
        token = infixexpr[i]
        print(token)
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while not opstack.isEmpty() and opstack.peek() != '(':
                postfixList.append(opstack.pop())
            opstack.pop()
        elif token in "+-*/":
            #先乘除后加减， 优先级高的先弹出. 再入栈

            while not opstack.isEmpty() and prec[token] < prec[opstack.peek()]:
                postfixList.append(opstack.pop())

            opstack.push(token)
        else:
            postfixList.append(token)
        i += 1
#中缀表达式单词列表扫描结束后，把opstack栈中的所有剩余操作符依次弹出，添加到输出列表末尾

    while not opstack.isEmpty():
        postfixList.append(opstack.pop())

    return " ".join(postfixList)

print(infixTOPostfix('(A+B)*C'))
print(infixTOPostfix('A*B+C*D'))
print(infixTOPostfix("(A+B)*C-(D-E)*(F+G)"))
# 'str' object is not callable
