# 用python实现ADT Stack

'''可以将List 的任意一端 （index=0 或者 -1）设置为栈顶
我们选用list的末端（index = -1）作为栈顶
这样栈的操作就可以通过list的append和pop来实现'''


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) -1]

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())



