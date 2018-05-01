# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-01 14:55:52
"""

#Z字型打印二叉树
#第一行从左到右，第二行从右到左
#方法：维护两个栈，奇数行(从0开始算行)先入右子树，再入左子树；
#偶数行，先入左子树，再入右子树
#奇数行入栈1，偶数行入栈2

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
    
def printBinTreeZ(p):
    if(p == None):  return
    
    stack1 = [p]
    stack2 = []
    
    while(stack1 != [] or stack2 != []):
        if(stack1 == []):   flag = 1
        if(stack2 == []):   flag = 0
        
        if(not flag):
            node = stack1.pop()
            print(node.x, end = " ")
            if(node.left):  stack2.append(node.left)
            if(node.right):  stack2.append(node.right)
        else:
            node = stack2.pop()
            print(node.x, end = " ")
            if(node.right):  stack1.append(node.right)  
            if(node.left):  stack1.append(node.left)

r = buildFromPreAndCen([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
printBinTreeZ(r)