# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 15:30:36
"""

# T56-2 数组中唯一只出现一次的数字
# 在一个数组中除了一个数字之外，其他数字都
# 出现了3次。请找出只出现一次的数字。

# 如果一个数字出现3次，那么它的二进制表示的
# 每一位也出现3次，那么如果把所有的二进制位
# 加起来，必定能被3整除。
# 把所有数字按数位相加，然后判断每一位能否被
# 3整除，如果能，则只出现一次的数字，该位为0
# 否则为1

def getNumAppOnce(nums):
    resu = ''
    for i in range(31):
        mask = 2 ** i
        times = 0
        for num in nums:
            if(mask & num != 0):
                times += 1
        resu += ('0' if times % 3 == 0 else '1')
    return int(resu[::-1], 2)
    
print(getNumAppOnce([1,1,1,3,3,2,3]))