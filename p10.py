'''
变位词： 两个词之间存在组成字母的重新排列关系
如 heart和earth， python和typhon
为了简单起见， 假设参与判断的两个词近由小写字母构成，而且长度相等

解题目标：
写一个bool函数， 以两个词作为参数， 返回这两个词是否为变位词

'''

'''
解法1: 逐字检查
将词1中的字符逐个到词2中检查是否存在
存在就“打勾”标记（防止重复检查）
如果每个字符都能找到，则两个词是变位词
只要有1个字符找不到，就不是变位词
'''
# 实现“打勾”标记：将词2对应字符设为None
# 由于字符串是不可变类型，需要先复制到列表中

def anagramSolution1(s1,s2):
    # 复制S2到列表
    alist = list(s2) # 查找list（）方法
    pos1 = 0
    stillOk = True
    #循环s1的每一个字符
    while pos1 < len(s1) and stillOk:
        pos2 = 0
        found = False
        #循环s2的每一个字符
        while pos2 < len(s2) and not found:
            if s1[pos1] == alist[pos2]: #在s2中逐个对比
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None
        else:
            stillOk = False
        pos1 = pos1 +1
    return stillOk

print(anagramSolution1('abcd','dcba'))

'''
解法二： 排序比较
将两个字符串都按照字母顺序排好序
再逐个字符对比是否相同，如果相同则是变位词
有任何不同就不是变位词
'''
def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
             pos += 1
        else:
            matches = False
    return matches

print(anagramSolution1('abcde','edcba'))





