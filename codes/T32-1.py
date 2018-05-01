# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-01 14:36:08
"""

#分行从上到下打印二叉树
#同样的用队列实现，维护一个换行符，每次换行符出队，
#打印之，并加到队尾，循环直到队列中只有一个换行符

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
        
def printBinTreeWide(p):
    if(p == None):  return
    
    queue = [p, "\n"]
    
    while(len(queue) > 1):
        now = queue[0]
        del queue[0]
        
        if(now == "\n"):
            print("")
            queue.append("\n")
        else:
            print(now.x, end = " ")
            if(now.left):   queue.append(now.left)
            if(now.right):  queue.append(now.right)

r = buildFromPreAndCen([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
printBinTreeWide(r)
