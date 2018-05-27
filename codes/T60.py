# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 19:13:17
"""

# T60 N个骰子的点数
# 把n个骰子扔在地上，所有骰子朝上的一面的点数之和
# 为s，输入为n，打印出s的所有可能的值出现的的概率。

# 两个数组，分别存储n-1个和n个骰子的点数和的次数
# 计算n个骰子点数和为s的次数时，需要将n-1个骰子
# s-1，s-2...s-6的个数加起来~

def getProbability(n):
    counts1 = [0 for i in range(6 * n + 1)]
    counts2 = [0 for i in range(6 * n + 1)]
    
    for i in range(1, 6 + 1):
        counts1[i], counts2[i] = 1, 1
    
    for i in range(2, n + 1):
        for j in range(i, i * 6 + 1):
            counts2[j] = sum(counts1[max(0, j - 6) : j])
        
        counts1[i-1], counts2[i-1] = 0, 0
        counts1[:] = counts2[:]
    
    return counts2
            