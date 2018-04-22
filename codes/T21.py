# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 16:04:41
"""

#调整数组的顺序，使得奇数在偶数前面
def changeOrder(X, func):
    if(len(X) == 0):
        return []
        
    i, j = 0, len(X) - 1
    
    while(i < j):
        while(func(X[i]) and i < j):
            i += 1
            
        while((not func(X[j])) and i < j):
            j -= 1
        
        if(i < j):
            X[i], X[j] = X[j], X[i]
    
    return X

def isEven(n):
    return n % 2 == 1

if __name__ == "__main__":
    testCase = [[1,2,3,4,5,6],
                [2,2,2,2,2,2],
                [2,4,6,1,3,4],
                [],
                [1],
                [2,1]]
    func = [isEven for i in range(len(testCase))]                
            
    print(list(map(changeOrder, testCase, func)))