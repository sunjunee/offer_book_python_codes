# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-21 20:12:24
"""

#旋转数组的最小数字

def getMinRotate(X):
    lens = len(X)
    i, j, mid = 0, lens - 1, 0
    
    while(X[i] >= X[j]):
        if(j - i == 1):
            mid = j            
            break
        
        mid = int((i + j) / 2)
        
        if(X[i] == X[mid] and X[j] == X[mid]):
            return X.index(min(X))
        
        if(X[i] > X[mid]):
            j = mid
        else:
            i = mid
            
    return mid
    
if __name__ == "__main__":
    testCase = [[3,4,5,1,2],
                [3,4,2],
                [7,8,2,3,4],
                [1,1,1,0,1]]
                
    
    print(list(map(getMinRotate, testCase)))