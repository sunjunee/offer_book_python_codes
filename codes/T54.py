# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-26 22:28:46
"""

# 面试题54：二叉搜索树的第k个结点
# 题目：给定一棵二叉搜索树，请找出其中的第k大的结点。

# 感觉就是中序遍历的修改版本

def getKthLargeInTree(root, k): 
    return search(root, k)
    
def search(p, k):
    target = None
    if(p.right):     
        target, k = search(p.right, k)
        
    if(target == None):
        if(k == 1):
            target = p
        k -= 1
    
    if(target == None and p.left != None):    
        target, k = search(p.left, k)
    
    return target, k
