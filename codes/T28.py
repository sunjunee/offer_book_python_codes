# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-30 17:16:10
"""

#判断一棵二叉树是否对称
#定义前序遍历的对称算法：先访问右节点，再访问左节点

#相当于，同时进行前序遍历
def isSymmetry(p1, p2):
    if(p1 == None and p2 == None):  return True
    
    if(p1 == None or p2 == None):  return False
    
    if(p1.x != p2.x):  return False
    
    return isSymmetry(p1.left, p2.right) and isSymmetry(p2.left, p1.right)
    
