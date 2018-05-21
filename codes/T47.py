# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-21 21:29:31
"""

# T47 礼物的最大价值
# 在一个m*n的棋盘的每一个都放一个礼物
# 每个礼物都有一定的价值，你可以从棋盘的左上角开始
# 拿礼物，并且每次向右或者向下移动一格，直到到达棋盘
# 的右下角，给定一个棋盘及其上面的礼物，求你最多能
# 拿到多少价值的礼物。

# 思路： 因为只能向右或者向下移动，因此对于某一个点的最大价值礼物
#        实际上等于从左边移动过来与从上面移动过来的礼物的价值的最大值
#       于是可以从左到右，从上到下计算每个点的最大礼物价值

def getMaxGiftValue(vals):
    w, h = len(vals[0]), len(vals)
    
    maxVal = [[0 for row in range(w)] for row in range(h)]

    for i in range(h):
        for j in range(w):
            maxVal[i][j] = vals[i][j] + max(getVal(maxVal, w, h, i - 1, j), getVal(maxVal, w, h, i, j - 1))
    
    return maxVal[h-1][w-1]
            
def getVal(maxVal, w, h, i, j):
    if(i >= 0 and i < h and j >= 0 and j < w):
        return maxVal[i][j]   
    return 0

if __name__ == "__main__":
    print(getMaxGiftValue([[1, 10, 3, 8],
                           [12, 2, 9, 6],
                           [5, 7, 4, 11],
                           [3, 7, 16, 5]]))