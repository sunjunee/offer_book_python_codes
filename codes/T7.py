# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-21 15:42:04
"""

#二叉树的基本操作
class TreeNode():
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

#构建二叉树
def create(root = None):  
    a = input();  
    if a is '#':  
        root = None;  
    else:  
        root = TreeNode(a);
        print(root.x, " -> left :", end = "")
        root.left = create(root.left);
        print(root.x, " -> right :", end = "")
        root.right = create(root.right);  
    return root;

#前序遍历二叉树：
def PreTravel(p):
    if(p == None):  return    
    print(p.x, end = " ")
    PreTravel(p.left)
    PreTravel(p.right)

#中通序遍历二叉树：
def CenTravel(p):
    if(p == None):  return    
    CenTravel(p.left)
    print(p.x, end = " ")
    CenTravel(p.right)

#后通序遍历二叉树：
def LatTravel(p):
    if(p == None):  return    
    LatTravel(p.left)
    LatTravel(p.right)
    print(p.x, end = " ")

#广度优先遍历：
def wideTravel(p):
    nodes_queue = [p]
    
    while(nodes_queue != []):
        node = nodes_queue[0]
        del nodes_queue[0]
        print(node.x, end = " ")
        if(node.left != None):  nodes_queue.append(node.left)
        if(node.right != None):  nodes_queue.append(node.right)
    

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
        

#print("Input a Node: ")
#r = create()
r = buildFromPreAndCen([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
print("先序遍历：", end = "")
PreTravel(r)
print("\n中序遍历：", end = "")
CenTravel(r)
print("\n后序遍历：", end = "")
LatTravel(r)
print("\n广度优先：", end = "")
wideTravel(r)
