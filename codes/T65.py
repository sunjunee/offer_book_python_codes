# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 21:08:49
"""

# T65 不使用加减乘除做加法
# 写一个函数，计算两个整数的和，不使用加减乘除

# 使用二进制的位运算来求解

def getSum(A, B):
    
    while(B):
        s = A ^ B
        c = (A & B) << 1
        A, B = s, c
        
    return A
        