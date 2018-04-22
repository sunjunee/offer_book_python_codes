# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 13:59:48
"""

#删除排序链表中的重复元素

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

#删除排序链表中的重复元素
def deleteReduntantNode(s):
    if(s == None):  return None
    
    p, c = s, s.next 

    while(c != None):
        if(p.x == c.x):
            #删除后节点
            c = c.next
            p.next = c
        else:
            p, c = p.next, c.next
    
    return s

if __name__ == "__main__":
    #构建链表
    nums = [1,1,1,2,2,2,2,2,2,2,2,3,3,4,5]
    s = bulidLinkList(nums)
    printLinkList(s)
    
    s = deleteReduntantNode(s)
    printLinkList(s)
