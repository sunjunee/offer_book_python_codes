# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-13 15:29:20
"""

# T39 数组中出现次数超过一半的数字
# 数组中有一个数字出现的次数超过了数组长度的一半

# 思路：存储一个数字，以及次数
# 如果下一个数字和存储的数字不相等，则次数减一
# 相等加一，如果次数为0，则换数字存储，并将次数置1

def getNumThanHalf(nums):
    cur, times = 0, 1
    for i, num in enumerate(nums):
        if(num == cur):
            times += 1
        else:
            times -= 1
            if(times == 0):
                cur = num
                times = 1
    
    return cur

if __name__ == "__main__":
    testCase = [[1, 2, 3, 3, 4, 3, 3],
                [1, 2, 2],
                [1, 1, 2]]

    print(list(map(getNumThanHalf, testCase)))
    