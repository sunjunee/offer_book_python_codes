# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-12 15:10:01
"""

#复杂链表的复制
#复杂链表中，每个节点除了有一个next指针指向下一个节点外，还有一个sibling指针指向
#链表中的任意一个节点或者null

class ListNode():
    def __init__(self, x):
        self.x = x
        self.next = None
        self.sibling = None
        
def copyLinkList(p):
    if(p == None):
        return
        
    start = p
    #第一步，在每个节点后复制一个该节点：
    while(p != None):
        node = ListNode(p.x)
        node.next, p.next = p.next, node
        p = node.next   #移动到下一节点
    
    #复制sibling指针的内容
    p = start
    while(p != None):
        p.next.sibling = p.sibling.next     #后一节点的sibling指向前一节点sibling的后一节点
        p = p.next.next
        
    #拆解为两个链表
    newStart = start.next
    p1 = start
    p2 = newStart
    
    while(p1 != None):
        p1.next = p1.next.next
        p2.next = p2.next.next
        p1 = p1.next
        p2 = p2.next
    
    return newStart

#没法测试啊。。。。