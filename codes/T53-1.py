# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-26 20:09:26
"""

# 面试题53（一）：数字在排序数组中出现的次数
# 题目：统计一个数字在排序数组中出现的次数。例如输入排序数组{1, 2, 3, 3,
# 3, 3, 4, 5}和数字3，由于3在这个数组中出现了4次，因此输出4。

# 排序数组，必选二分法

def getTimesOfNum(nums, n):
    pos = FindPos(nums, n) - 1
    count = 0
    if(pos >= 0 and nums[pos] == n):
        count = 1
        pre, nex = pos - 1, pos + 1
        while(pre >= 0 and nums[pre] == n):
            count += 1
            pre -= 1
        while(nex < len(nums) and nums[nex] == n):
            count += 1
            nex += 1
    return count
    
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
    print(getTimesOfNum([1, 2, 3, 3, 3, 3, 4, 5], 5))