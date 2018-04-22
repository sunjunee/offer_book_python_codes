# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 17:35:23
"""

# 树的子结构
# 输入两颗二叉树A和B，判断B是不是A的子结构

def judge(a, b):
    if(b == None):
        return True
    if(a == None):
        return False
    
    if(a.x != b.x):
        return False
    
    return judge(a.left, b.left) and judge(a.right, b.right)

def judgeAB(A, B):  #类似于先序遍历
    if(A == None or B == None):  return False
    
    if(A.x == B.x):
        resu = judge(A, B)
    if(not resu):
        resu = judgeAB(A.left, B)
    if(not resu):
        resu = judgeAB(A.right, B)

