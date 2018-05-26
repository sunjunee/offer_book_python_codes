# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-26 19:17:15
"""

# 面试题51：数组中的逆序对
# 题目：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组
# 成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

# 思路： 从头到尾遍历数组，用一个数组存储前n个排序的结果，对于第n+1个数，
#       其组成的逆序对数，就是其后面的数字的个数

def getReversePairs(nums):
    pairs = 0    
    sortedNums = []
    for i, num in enumerate(nums):
        pos = FindPos(sortedNums, num)
        pairs += i - pos
        sortedNums.insert(pos, num)
    return pairs
    

def FindPos(sortedNums, num):
    lens = len(sortedNums)
    if(lens == 0):  return 0
    
    start, end = 0, lens - 1
    while(end - start > 1):
        center = int((end + start) / 2)
        if(sortedNums[center] == num):
            return center + 1
        elif(sortedNums[center] < num):
            start = center
        else:
            end = center
            
    if(sortedNums[start] > num):
        return start
    elif(sortedNums[start] <= num and num < sortedNums[end]):
        return start + 1
    else:
        return end + 1
             
if __name__ == "__main__":
    print(getReversePairs([1, 0, -1, 0, -2, 8]))