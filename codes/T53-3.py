# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 14:05:53
"""

# 数组中数值和下标相等的元素
# 结社一个单调递增的数组里，每个元素都是整数且
# 唯一，请编写一个函数，找出数组中任意一个数值
# 等于其下标的元素，例如：在数组{-3, -1, 1, 3, 5}
# 中，数字3和它的下标相等。

# 同样使用二分法来求解

def getNumSameWithIndex(nums):
    lens = len(nums)
    if(lens == 0):  return None
    
    start, end = 0, lens - 1
    
    while(start <= end):
        center = (start + end) // 2
        if(nums[center] == center):
            return center
        elif(nums[center] > center):
            end = center - 1
        else:
            start = center + 1
    
    return None