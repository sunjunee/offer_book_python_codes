# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 10:15:59
"""

#矩阵中的路径判断

def judgePath(arrayList, string):
    m, n = len(arrayList), len(arrayList[0])
    
    
    for i in range(m):
        for j in range(n):
            visited = [[0 for i in range(n)] for m in range(m)]
            if (judge(arrayList, m, n, i, j, string, 0, visited)):
                return 1
    
    return 0
            
def judge(arrayList, m, n, i, j, string, l, visited):
    if(i > m - 1 or i < 0 or j > n - 1 or j < 0):
        return 0
    
    if(arrayList[i][j] != string[l] or visited[i][j] == 1):
        return 0
    
    if(l == len(string) - 1):
        return 1
    
    visited[i][j] = 1
    
    resu = (judge(arrayList, m, n, i - 1, j, string, l + 1, visited) or 
            judge(arrayList, m, n, i + 1, j, string, l + 1, visited) or
            judge(arrayList, m, n, i, j - 1, string, l + 1, visited) or
            judge(arrayList, m, n, i, j + 1, string, l + 1, visited))
            
    if(not resu):
        visited[i][j] = 0
    
    return resu
    
if __name__ == "__main__":
    arrayList = [["a", "b", "t", "g"],
                ["c", "f", "c", "s"],
                ["j", "d", "e", "h"]]
                
    testCases = ["bfcs", "tgscedj", "a", "abddd"]
    arrayList = [arrayList for i in range(len(testCases))]
    print(list(map(judgePath, arrayList, testCases)))
                