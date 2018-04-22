# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-21 14:59:52
"""

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

#插入节点
def insertNode(s, before_x, insert_x):
    #在值为before_x之后添加insert_x的节点
    p = s
    while(p != None):
        if(p.x == before_x):
            nex = p.next
            p.next = ListNode(insert_x)
            p.next.next = nex
            break
        p = p.next
    
    return s

#删除节点
def deleteNode(s, delete_x):
    p = s
    
    tem = ListNode(0)
    tem.next = s
    s = tem
    b = s    
    
    while(p != None):
        if(p.x == delete_x):
            b.next = p.next
            break
        b = p            
        p = p.next
    
    return s.next

#修改节点的值
def modifyNode(s, before_x, after_x):
    p = s
    while(p != None):
        if(p.x == before_x):
            p.x = after_x
            break
        p = p.next
        
    return s

if __name__ == "__main__":
    #构建链表
    nums = [1,2,3,4,5,6,8,9]
    s = bulidLinkList(nums)
    printLinkList(s)
    
    #增加节点: 在6的后面加7
    s = insertNode(s, 6, 7)
    printLinkList(s)    
    
    #删除节点:删除值为9的节点
    s = deleteNode(s, 9)
    printLinkList(s)
        
    #修改节点:将第一个取值为2的点修改为9
    s = modifyNode(s, 2, 9)
    printLinkList(s)