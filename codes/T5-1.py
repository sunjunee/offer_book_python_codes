# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-21 14:41:07
"""

#两个排序的数组A1和A2，把A2中的所有数字插入A1,并保持排序

def mergeArray(A1, A2):
    l1, l2 = len(A1), len(A2)
    A1 = A1 + A2    # 假设通过这种方法在A1后面加上A2的空间     
    i, j = l1 - 1, l2 - 1
    c = l1 + l2 - 1
    while(True):
        if(i >= 0 and j >= 0):
            if(A1[i] > A2[j]):
                A1[c] = A1[i]
                i -= 1
            else:
                A1[c] = A2[j]
                j -= 1
            c -= 1
        elif(i < 0):
            A1[0:(j + 1)] = A2[0:(j + 1)]
            break
        else:
            break
    
    return A1

#if __name__ == "__main_":
A1 = [[1, 2, 3], [2, 5, 9], [0, 3, 10]]
A2 = [[0, 6, 7], [1, 1, 1], [2, 3, 9]]

print(list(map(mergeArray, A1, A2)))