# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-01 15:35:01
"""

#二叉搜索树的后序遍历序列
#输入一个整数数组，判断该数组是不是某二叉搜索树的
#后序遍历结果。如果是则返回True，否则返回False，
#假设输入的任意两个数字都不相同

#思路： 二叉搜索树的后序遍历，对于当前的数组，最后一个节点是根节点，
# 前面的节点，可以分为两部分，最前面小于该节点的为左子树，后面大于它的为右子树。
# 需要找到一个分割点，将前面的节点分为其左右子树。
# 对于每一个根节点，需要作上述判断，找到左右子树，然后递归。

def judgeSearchTreeBack(A):
    if(len(A) == 0):    return False
    return judge(A, 0, len(A) - 1)

def judge(A, start, end):
    if(start == end):   return True
    
    root = A[end]
    #找到左右子树
    for i in range(start, end + 1): #这里是为了让全部为左子树的特殊情况，满足下面root的判断。
        if(A[i] > root):
            break
    
    #判断右子树是否有小于root的值
    for j in range(i, end):
        if(A[j] < root):
            return False
    
    left, right = True, True
    if(i > start):
        left = judge(A, start, i - 1)
    if(end > i):
        right = judge(A, i, end - 1)

    return left and right

if __name__ == "__main__":
    testCase = [[5, 7, 6, 9, 11, 10, 8],
                [7, 4, 6, 5],
                [2, 3, 4, 6]]
    
    print(list(map(judgeSearchTreeBack, testCase)))