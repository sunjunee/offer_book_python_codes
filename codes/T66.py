# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 21:09:50
"""

# T66 构建乘积数组
# 给定一个数组A[0,1,...n-1]，构建一个数组B[0,1,2...n-1]
# 其中B的元素B[i] = A[0]*A[1]...A[i-1]*A[i+1]*...A[n-1]
# 不能使用除法

def getMultipleArray(A):
    lens = len(A)
    tem1, tem2 = [1, A[0]], [1, A[-1]]
    for i in range(1, lens-1):
        tem1.append(tem1[-1] * A[i])
        tem2.append(tem2[-1] * A[lens - i - 1])
    
    B = []
    
    for i in range(len(tem1)):
        B.append(tem1[i] * tem2[len(tem2) - 1 - i])
    
    return B

print(getMultipleArray([1,2,3,4,5]))