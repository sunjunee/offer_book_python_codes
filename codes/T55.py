# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-26 22:39:44
"""

# 面试题55（一）：二叉树的深度
# 题目：输入一棵二叉树的根结点，求该树的深度。从根结点到叶结点依次经过的
# 结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

def getTreeDepth(root):
    return search(root)
    
def search(p):
    if(p == None):
        return 0
    
    return 1 + max(search(p.left), search(p.right))

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

r = buildFromPreAndCen([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
print(getTreeDepth(r))

#        1
#       / \
#      2   3
#     /   /\
#    4   5  6
#     \    /
#      7  8