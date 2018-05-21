# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-16 21:51:37
"""

# T45 把数组排成最小的数
# 输入一个正整数数组，把数组里面所有的数字拼接成一个数，
# 打印出能拼接出的最小数。

# 思路：相当于对数组中的数，按照“从小到大”的顺序排列
# 只是大小之分需要重新定义
# 从左到右，高位越大，认为其值越大

def getMinNum(nums):
    #排序：
    lens = len(nums)
    for i in range(lens):
        for j in range(lens - 1 - i):
            if(Comapare(nums[j], nums[j + 1])):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
    return "".join([str(n) for n in nums])
    
def Comapare(a, b):
    a, b = str(a), str(b)
    return True if a + b >= b + a else False


if __name__ == "__main__":
    print(getMinNum([34, 2, 35, 24, 241, 10]))