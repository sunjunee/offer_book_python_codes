# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-21 15:32:43
"""

#从尾到头打印链表

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

#从尾到头打印节点
def printFromTail(s):
    if(s == None):
        return
    else:
        printFromTail(s.next)
        if(s.next == None):
            print(s.x, end = "")
        else:
            print(" <- ", s.x, end = "")

if __name__ == "__main__":
    #构建链表
    nums = [1,2,3,4,5,6,8,9]
    s = bulidLinkList(nums)
    printLinkList(s)
    printFromTail(s)