# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 14:56:10
"""

# T56-1 数组中数字出现的次数
# 数组中只出现一次的两个数字
# 一个整型数组中除了两个数字外，其他数字都出现了两次。
# 请找出这两个只出现一次的数字，要求时间复杂度为O(n)
# 空间复杂度为O(1)

# 两个相同的数，异或之后为0
# 一个数与0异或还是其本身。

# 先把所有数字异或，然后得到的数字，
# 至少有一位为1
# 把数字按照这一位为0和为1分为两组
# 然后两组分别异或，得到两个不同的数

def getNumAppOnce(nums):
    tem = XOR(nums)
    i = bin(tem)[2:].index('1')     #找到一个不为0的位
    i = len(bin(tem)[2:]) - i - 1
    tem = int('1' + '0' * i if i > 0 else '1', 2)
    print(len(bin(tem)) - 2, tem)
    
    nums1, nums2 = [], []
    
    for num in nums:
        if(num & tem):
            nums1.append(num)
        else:
            nums2.append(num)
            
    return XOR(nums1), XOR(nums2)
            
def XOR(nums):
    resu = 0
    for num in nums:
        resu ^= num
    return resu

print(getNumAppOnce([1,1,2,2,3,3,10,5,5,9]))