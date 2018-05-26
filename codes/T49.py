# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-23 09:22:12
"""

# T49 丑数
# 我们把只包含因子2,3,5的数称为丑数，求按从小到大的顺序的第
# 1500个丑数，例如：6、8都是丑数，但14不是，因为它包含因子7.
# 习惯上我们把1当做第一个丑数。

# 思路：每一个丑数都可以由前面的某个丑数，乘以2/3/5得到。
# 由于前面得到的丑数是从小到大排列的，因此维护3个index，
# 用来保存被乘以2/3/5的位置，每次获取下一个丑数的时候，
# 去比较三个位置得到的数的最小值。实际上前面生成的丑数，
# 可以用三个队列来存。

def getUglyNum(index):
    if(index < 0):  return None

    uglyNums = [1]
    p2, p3, p5 = 0
    while(len(uglyNums) < index):
        minNum = min([uglyNums[p2] * 2, uglyNums[p3] * 3, uglyNums[p5] * 5])
        uglyNums.append(minNum)
        while(uglyNums[p2] * 2 <= minNum):
            p2 += 1
        while(uglyNums[p3] * 3 <= minNum):
            p3 += 1
        while(uglyNums[p5] * 5 <= minNum):
            p5 += 1
    
    return minNum