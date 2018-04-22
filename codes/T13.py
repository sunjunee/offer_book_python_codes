# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 10:51:42
"""

#机器人运动范围

def judgeDigits(i, j, k):
    i, j = str(i), str(j)
    digits = i + j
    s = sum([int(d) for d in digits])
    if(s > k):
        return 1
    else:
        return 0

def getAreas(m, n, i, j, visited):
    if(i < 0 or i > m - 1 or j < 0 or j > n - 1):
        return 0
    
    if(visited[i][j] == 1 or judgeDigits(i, j, 18)):
        return 0
    
    visited[i][j] = 1
    return 1 + (getAreas(m, n, i - 1, j, visited) + 
                getAreas(m, n, i + 1, j, visited) + 
                getAreas(m, n, i, j + 1, visited) +
                getAreas(m, n, i, j - 1, visited))

def counting(m, n):
    visited = [[0 for i in range(n)] for j in range(m)]
    return getAreas(m, n, 0, 0, visited)

if __name__ == "__main__":
    m = [20, 10, 8, 40, 30]
    n = [30, 40, 30, 9, 30]
    
    print(list(map(counting, m, n)))