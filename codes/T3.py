# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-21 10:45:50
"""

# 找出数组中任意一个重复的数字
# n个数字都在0 - n-1范围内

# 修改数组：Time: O(n), Space: O(1)
def getRepet(X):
    n = len(X)
    for i in range(n):
        while(X[i] != i):
            t = X[i]
            if(X[t] == X[i]):
                return X[i]
            X[i], X[t] = X[t], X[i]


# 不修改数组：Time: O(nlogn), Space: O(1)
def getRepet1(X):
    n = len(X)
    start = 0
    end = n - 1
    
    while(start < end):
        #计算start到middle的个数
        middle = int((start + end) / 2)
        tem = 0
        for a in X:
            if(a >= start and a <= middle):
                tem += 1
        if(tem > middle - start + 1):
            end = middle
        else:
            start = middle + 1
            
    return start

if __name__ == "__main__":
    testCase = [[4,3,1,0,2,5,3],
                [0,1,2,2,1,3],
                [0,0],
                [1,2,3,0,1]]
    
    print(list(map(getRepet, testCase)))
    print(list(map(getRepet1, testCase)))