# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 20:17:41
"""

# T62 圆圈中最后剩下的数字
# 0~n-1这n个数字排成一个圆圈。从数字0开始，每次从圆圈里删除
# 第m个数字，求最后圆圈剩下的数字。

# 在这n个数字中，第一个被删除的数字是(m-1) % n，记为k，删除k之后
# 剩下的序列是0,1,2...k-1,k+1,...n-1，下一次删除开始时，序列为
# k+1,...n-1,0,1,...k-1.我们将其映射为0,1,2....n-2，p(x) = (x-k-1) % n
# 逆映射为(x + k + 1) % n
# 所以对于f(n,m)有， f(n,m) = [f(n-1, m) + m] % n

def getTheLastNum(n, m):
    if(n < 1 or m < 1):
        return -1
    
    last = 0
    for i in range(2, n + 1):
        last = (last + m) % i
    return last