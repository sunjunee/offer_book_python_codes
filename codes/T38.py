# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-13 12:28:44
"""

# T38 字符串的排列（全排列问题）
# 输入一个字符串，打印出该字符串中字符的所有排列。

# 思路： 全排列问题的思路，一般都是递归实现。
# 对于ABCDE， 先考虑A开头，然后B开头，...E开头。即：A分别与其他字符换位置
# 然后对于A开头，分别考虑B,C,D,E开头。
# 然后对于AB开头，分别考虑C,D,E
# ... 可以用递归实现。

def allCaseOfSorting(strs):
    printCases(strs, 0)

def printCases(strs, index):
    if(index == len(strs) - 1):
        print(strs)
        return
    
    for i in range(index, len(strs)):
        strs[i], strs[index] = strs[index], strs[i]
        printCases(strs, index + 1)
        strs[i], strs[index] = strs[index], strs[i]

if __name__ == "__main__":
    allCaseOfSorting([1, 2, 4])