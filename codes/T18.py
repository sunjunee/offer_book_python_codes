# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 13:40:31
"""

#在O(1)时间内删除链表的节点
#给定链表的头结点和要删除的节点指针

#链表的节点
class ListNode():
    def __init__(self, x):
        self.x = x
        self.next = None

#构建链表    
def bulidLinkList(nums):
    if(len(nums) == 0):
        return None
    else:
        s = p = ListNode(nums[0])
        for n in nums[1:]:
            p.next = ListNode(n)
            p = p.next
        return s

#打印节点
def printLinkList(s):
    if(s == None):
        return
    else:
        while(s != None):
            if(s.next != None):
                print(s.x, " -> ", end = "")
            else:
                print(s.x)
            s = s.next

#删除指定节点:将后一节点的信息复制到前面，然后删除后面节点，特例是尾巴
def deleteNode(s, p):
    
    if(p.next != None):
        p.x = p.next.x
        p.next = p.next.next
    else:
        if(s == p):
            return None
        t = s
        while(t.next != p):
            t = t.next
        t.next = None
    
    return s

if __name__ == "__main__":
    #构建链表
    nums = [1,2,3,4,5]
    s = bulidLinkList(nums)
    printLinkList(s)
    
    s = deleteNode(s, s)
    printLinkList(s)
