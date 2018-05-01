# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-23 08:50:58
"""

#树的镜像：在原树的基础上直接修改
def buildMirror(p):
    if(p == None):  return
    
    if(p.left == None and p.right == None):
        return
    
    p.left, p.right = p.right, p.left
    if(p.left):
        buildMirror(p.left)
    if(p.right):
        buildMirror(p.right)
