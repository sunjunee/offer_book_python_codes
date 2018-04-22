# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-21 12:40:34
"""

#二维数组中的查找
def findInTwoDim(X, num):
    m, n = len(X), len(X[0])
    
    i, j = 0, n - 1
    
    while(i <= m - 1 and j >= 0):
        if(X[i][j] == num):
            print(i, j)
            break
        else:
            if(X[i][j] > num):  #左移
                j -= 1
            else:               #右移
                i += 1

if __name__ == "__main__":
    findInTwoDim([[1, 2, 7, 8],
                  [2, 4, 9, 12],
                  [4, 7, 10, 13],
                  [6, 8, 11, 15]], 10)
        