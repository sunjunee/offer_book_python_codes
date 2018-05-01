# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-01 09:57:06
"""

#顺时针打印矩阵
#从4个方向打印即可

def printArrayCW(a):
    w, h = len(a[0]), len(a)
    p1, p2 = [0, 0], [h - 1, w - 1]
    
    while(p1[0] <= p2[0] and p1[1] <= p2[1]):
        printCW(a, p1, p2)
        p1[0] += 1
        p1[1] += 1
        p2[0] -= 1
        p2[1] -= 1
        
    print("\n")

def printCW(a, p1, p2):   
    for i in range(p1[1], p2[1]):
        print(a[p1[0]][i], end=" ")
    
    for i in range(p1[0], p2[0] + 1):
        print(a[i][p2[1]], end=" ")
        
    if(p2[0] > p1[0]):  #有两列
        for i in range(p2[1] - 1, p1[1] - 1, -1):
            print(a[p2[0]][i], end=" ")
            
    if(p2[1] > p1[1]):  #有两行
        for i in range(p2[0] - 1, p1[0], -1):
            print(a[i][p1[1]], end=" ")

if __name__ == "__main__":
    testCase = [[[1,2,3],
                [4,5,6],
                [7,8,9]],
                
                [[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]],

                [[1,2,3],
                 [4,5,6],
                 [7,8,9],
                 [10,11,12]],

                [[1,2],
                 [4,5],
                 [7,8],
                 [10,11]]]
                 
    list(map(printArrayCW, testCase))