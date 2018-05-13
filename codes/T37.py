# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-13 11:00:00
"""

# T37 请实现两个函数，分别用来序列化和反序列化二叉树
# 序列化：二叉树 --> 字符串
# 反序列化：字符串 --> 二叉树
# 原先的二叉树前序与后序遍历，重建一颗二叉树，其中不能有重复的节点
# 因此对于通用的做法，是不能通过这种方法来重建的

#思路：使用先序遍历读取二叉树，对于为空的子树，打印特殊符号

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
###################################################################################
###################################################################################

#序列化
def serialize(p, seris):
    if(p == None):
        seris.append(None)
        return
    
    seris.append(p.x)
    
    serialize(p.left, seris)
    serialize(p.right, seris)

#反序列化
def deSerialize(seris):
    start = [0]     #在函数之间传递值
    return process(seris, start)

def process(seris, start):
    if(seris[start[0]] == None):
        start[0] = start[0] + 1
        return None
    
    node = TreeNode(seris[start[0]])
    start[0] = start[0] + 1

    node.left = process(seris, start)
    node.right = process(seris, start)
    
    return node
    
    
if __name__ == "__main__":
    r = buildFromPreAndCen([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])    #构建树
    
    #序列化    
    seris = []    
    serialize(r, seris)
    print(seris)
    
    #反序列化
    t = deSerialize(seris)
    printBinTreeWide(t)
    
#     1
#    / \
#   2   3
#  /   / \
# 4   5   6
#  \     /
#   7   8