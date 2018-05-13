# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-12 15:43:01
"""

#二叉搜索树与双向链表
#输入一颗二叉搜索树，将该二叉搜索树转换成一个排序的双向链表
#不能创建任何节点，只能调整树中节点指针的指向

#思路：二叉树节点，使左子树小，右子树大。
#使用递归，类似树的中序遍历进行实现

def tranSearchTreeToLinkList(p):
    lastNode = [None]
    trans(p, lastNode)
    
    s = lastNode[0]
    while(s.left):
        s = s.left

    return s
    
def trans(p, lastNode):
    if(p == None):  return
    
    cur = p
    
    if(cur.left):     
        trans(cur.left, lastNode)
    
    cur.left = lastNode[0]
    if(lastNode[0]):  
        lastNode[0].right = cur

    lastNode[0] = cur
    
    if(cur.right):
        trans(cur.right, lastNode)
    