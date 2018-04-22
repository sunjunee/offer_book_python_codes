# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 17:28:03
"""

#合并两个排序的链表

#并不难，维护三个指针即可:可以在前面多加一个节点，简化操作

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
            
def mergetTwoSortList(s1, s2):
    s = ListNode(0)
    p = s
    while(s1 != None and s2 != None):
        if(s1.x > s2.x):
            p.next = s2
            s2 = s2.next
        else:
            p.next = s1
            s1 = s1.next
        p = p.next
    
    if(s1 != None):
        p.next = s1
    if(s2 != None):
        p.next = s2
            
    return s.next

if __name__ == "__main__":
    nums1 = [1,2,3,6,7,9]
    nums2 = [3,4,4,5,10]
    s1 = bulidLinkList(nums1)
    printLinkList(s1)
    s2 = bulidLinkList(nums2)
    printLinkList(s2)
    
    s = mergetTwoSortList(s1, s2)
    printLinkList(s)     
      
            