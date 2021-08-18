# 变位词判断问题
'''
❖暴力法解题思路为：穷尽所有可能组合
❖将s1中出现的字符进行全排列，再查看s2
是否出现在全排列列表中
❖这里最大困难是产生s1所有字符的全排列
根据组合数学的结论，如果n个字符进行全排列
，其所有可能的字符串个数为n!
'''
# 解法四: 计数比较
'''❖解题思路：对比两个词中每个字母出现的
次数，如果26个字母出现的次数都相同的
话，这两个字符串就一定是变位词
❖具体做法：为每个词设置一个26位的计数
器，先检查每个词，在计数器中设定好每
个字母出现的次数
❖计数完成后，进入比较阶段，看两个字符
串的计数器是否相同，如果相同则输出是
变位词的结论
'''
# ord()
# In Python, the ord () function accepts a string of unit length as an argument
# and returns the Unicode equivalence of the passed argument.

def anagramSolution4(s1,s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1
    j = 0
    stillOk = True
    while j < len(c1):
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOk = False
    return stillOk
print(anagramSolution4('apple', 'pleap'))






