# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 13:25:23
"""

# T53-2 0-n-1中缺失的数字
# 一个长度为n-1的递增排序数组中所有数字都是唯一的，
# 并且每个数字都在0-n-1范围内，且其中有且仅有一个
# 数字不在该数组内，请找出这个数字

def getLostDigit(nums):
    lens = len(nums)
    if(lens == 0):  return None
    if(nums[0] == 1):   return 0
    if(nums[-1] == lens - 1):   return lens
       
    start, end = 0, lens - 1
    while(end - start != 1):
        center = (start + end) // 2
        if(nums[center] == center):
            start = center
        else:
            end = center
    
    return end
        