# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-30 15:43:23
"""

#二叉树的遍历问题：前序、中序、后序（递归、非递归实现）

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

#中序遍历二叉树：
def CenTravel(p):
    if(p == None):  return    
    CenTravel(p.left)
    print(p.x, end = " ")
    CenTravel(p.right)

#后序遍历二叉树：
def LatTravel(p):
    if(p == None):  return    
    LatTravel(p.left)
    LatTravel(p.right)
    print(p.x, end = " ")

#非递归前序遍历：依次访问栈顶元素、打印，访问该节点的右子树、左子树，入栈。
def PreTravelNoRecu(p):
    if(p == None): return
    
    stack = [p]
    
    while(stack != []):
        node = stack.pop()
        print(node.x)
        
        if(node.right): stack.append(node.right)
        if(node.left):  stack.append(node.left)

#非递归中序遍历：
#1、如果栈顶元素非空且左节点存在，将其入栈，重复该过程。若不存在则进入第2步
#2、若栈非空，输出栈顶元素并出栈。判断刚出栈的元素的右节点是否存在，不存在重
#复第2步，存在则将右节点入栈，跳至第1步

def CenTravelNoRecu(p):
    if(p == None): return
    
    stack = [p]
    
    while(stack != []):
        
        while(stack != []):
            node = stack[-1]
            if(node.left):  
                stack.append(node.left)
        
        while(stack != []):
            node = stack[-1]
            stack.pop()
            print(node.x)
            if(node.right):
                stack.append(node.right)
                break


#非递归后序遍历：
#1、如果栈顶元素非空且左节点存在，将其入栈，重复该过程。若不存在则进入第2步（该过程和中序遍历一致）
#2、判断上一次出栈节点是否当前节点的右节点，或者当前节点是否存在右节点，满足任一条件，将当前节点输出,
#并出栈。否则将右节点压栈。跳至第1步

def LatTravelNoRecu(p):
    if(p == None): return
    
    stack = [p]
    laspop = None
    
    while(stack != []):
        
        while(stack != []):
            node = stack[-1]
            if(node.left):  
                stack.append(node.left)
        
        while(stack != []):
            if(laspop == stack[-1].right or stack[-1].right == None):
                print(stack[-1].x)
                laspop = stack[-1]
                stack.pop()
            elif(stack[-1].right != None):
                stack.append(stack[-1].right)
                break

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
