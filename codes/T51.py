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
            #如果相等，则找最右边相等的位置
            c = center
            while(sortedNums[c] == num):
                c += 1
            return c
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

################# 书上解法 ##################
# 使用归并排序的思想，将数组二分，然后计算前一部分
# 与后一部分之间的逆序对数目
def getReversePairs_1(nums):
    return mergeSort(nums, 0, len(nums) - 1)

def mergeSort(nums, start, end):
    if(start == end):
        return 0
    
    pairs = 0
    center = int((start + end) / 2)
    pairs += mergeSort(nums, start, center)
    pairs += mergeSort(nums, center + 1, end)
    
    newNums = []
    i, j = start, center + 1
    while(i <= center and j <= end):
        if(nums[i] > nums[j]):
            newNums.append(nums[j])
            pairs += (center - i + 1)
            j += 1
        else:
            newNums.append(nums[i])
            i += 1
    if(i > center):
        newNums.extend(nums[j:end+1])
    else:
        newNums.extend(nums[i:center+1])
    nums[start : end + 1] = newNums
    return pairs

if __name__ == "__main__":
    print(getReversePairs_1([7,5,5,5,5,6,4, 3]))