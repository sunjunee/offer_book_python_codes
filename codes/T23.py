# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 16:38:18
"""

#寻找链表中环的入口

#方法：分三步走策略：1、双指针法找到环内的一个点
#                 2、单指针计算环中的节点数
#                 3、双指针法，一个先走环的节点数步，然后一起走，直到相遇。

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

def getLastNode(s, n):
    if(s == None):  return None
    
    p1 = p2 = s
    for i in range(n):
        if(p1 == None):
            return None
        p1 = p1.next
    
    while(p1 != None):
        p1 = p1.next
        p2 = p2.next
    
    return p2

def getLoopStart(s):
    if(s == None):  return None
    
    p1, p2 = s, s.next
    
    #找到环内一个节点
    while(p1 != p2):
        p1 = p1.next
        p2 = p2.next.next
    
    #计算环长：
    c = 1
    while(p2.next != p1):
        p2 = p2.next
        c += 1
    
    #双节点，一个先走c步
    p1 = p2 = s
    for i in range(c):
        p1 = p1.next
    
    while(p1 != p2):
        p1 = p1.next
        p2 = p2.next
        
    return p1
    

if __name__ == "__main__":
    #构建链表
    nums = [9,8,7,6,5,4,3,2,1]
    s = bulidLinkList(nums)
    printLinkList(s)
    
    #构建环 1->6
    p1 = getLastNode(s, 1)
    p2 = getLastNode(s, 3)
    p1.next = p2
    
    #找环入口
    print(getLoopStart(s).x)
    