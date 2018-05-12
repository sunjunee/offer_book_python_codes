# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-12 14:35:01
"""

#二叉树中和为某一值的路径
#输入一颗二叉树和一个整数，打印二叉树中节点值得和为输入整数的所有路径
#从树的根节点一直往下一直到叶子节点所经过的节点形成一条路径

#思路：实际上就是遍历一遍二叉树

###################################################################################
###################################################################################
class TreeNode():
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

def bulid(pre, cen, startCen, endCen):    
    #在前序遍历中，找出当前要取的根节点及其取值
    nums = cen[startCen : endCen+1]
    rootIndex = min(list(map(lambda x : pre.index(x), nums)))
    rootValue = pre[rootIndex]
    
    #根节点在中序中的位置：
    rootIndexCen = cen.index(rootValue)
    #构建节点
    root = TreeNode(rootValue)    
    #构建左子树
    if(startCen <= rootIndexCen - 1):
        root.left = bulid(pre, cen, startCen, rootIndexCen - 1)
    #构建右子树
    if(rootIndexCen + 1 <= endCen):
        root.right = bulid(pre, cen, rootIndexCen + 1, endCen)
    
    return root
    
#根据前序遍历结果和中序遍历结果构建二叉树：
def buildFromPreAndCen(pre, cen):
    startCen = 0
    endCen = len(cen) - 1
    return bulid(pre, cen, startCen, endCen)
###################################################################################
###################################################################################

def printRouteWithValue(p, x):
    judge(p, 0, x, [])

def judge(p, curVal, x, path):
    if(p.left == None and p.right == None): #为叶子节点
        if(p.x + curVal == x):
            path.append(p.x)
            for n in path:
                print(n)
            path.pop()
    else:
        #递归左右子树
        path.append(p.x)
        
        if(p.left):
            judge(p.left, curVal + p.x, x, path)
        if(p.right):
            judge(p.right, curVal + p.x, x, path)
        
        path.pop()

if __name__ == "__main__":
    r = buildFromPreAndCen([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])    #构建树
    printRouteWithValue(r, 14)

#     1
#    / \
#   2   3
#  /   / \
# 4   5   6
#  \     /
#   7   8