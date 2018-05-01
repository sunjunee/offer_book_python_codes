# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-01 14:30:46
"""

#从上到下打印二叉树
#暂且称之为二叉树的广度优先遍历
#用一个队列来进行实现

def printBinTreeWide(p):
    if(p == None):  return
    
    queue = [p]
    while(queue != []):
        node = queue[0]
        del queue[0]
        print(node.x, end = "")

        if(node.left):  queue.append(node.left)
        if(node.right): queue.append(node.right)        