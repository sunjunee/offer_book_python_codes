# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-13 18:58:49
"""

# T42 连续子数组的最大和
# 输入一个整型数组，数组里有正数也有负数。
# 数组中的一个或者多个整数组成一个子数组。
# 求所有子数组的和的最大值。时间复杂度为O(n)

# 动态规划问题：
# 考虑fi为以i结尾的子数组的最大和
# 则fi = nums[i] if (fi-1 < 0) else fi-1 + nums[i]

def getMaxSum(nums):
    fi = nums[0]
    maxsum = fi
    for num in nums[1:]:
        if(fi < 0):
            fi = num
        else:
            fi = fi + num
        if(fi > maxsum):
            maxsum = fi
    return maxsum

print(getMaxSum([1, 2, -2, 8, 7, -2, 9]))