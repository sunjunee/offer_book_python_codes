# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 17:05:45
"""

#反转链表

#基本操作，注意边界条件

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

#反转链表
def tranverse(s):
    if(s == None):   return None
    
    pre, cur, pre.next = s, s.next, None
    
    while(cur != None):
        nex, cur.next= cur.next, pre
        pre, cur = cur, nex
    
    return pre

if __name__ == "__main__":
    nums = [9,8,7,6,5,4,3,2,1]
    s = bulidLinkList(nums)
    printLinkList(s)
    
    s = tranverse(s)
    printLinkList(s)