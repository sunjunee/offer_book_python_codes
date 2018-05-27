# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 15:55:11
"""

# T57 和为S的数字
# T57-1 输入一个递增排序的数组和一个数字s
# 在数组中查找两个数，使得它们的和正好是s
# 如果有多对数字的和等于s，则输出任意一对
# 即可。

# 两个index，分别在最左和最右，每次比较当前
# index的两个数的和，与s的大小关系，然后移动
# 两个index

def getNumsOfSumS(nums, s):
    lens = len(nums)
    
    i, j = 0, lens - 1
    
    while(i < j):
        tem = nums[i] + nums[j]
        if(tem == s):
            return nums[i], nums[j]
        elif(tem > s):
            j -= 1
        else:
            i += 1
            
    return None

print(getNumsOfSumS([0,2,3,5,6,9,10], 7))