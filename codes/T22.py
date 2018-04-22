# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 16:16:51
"""

#输出链表中倒数第k个节点
#链表中的节点从1开始计数

#方法：双指针法，前指针先走k步，然后一起走，直到前指针指向尾巴（p->next == None）

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

if __name__ == "__main__":
    #构建链表
    nums = [9,8,7,6,5,4,3,2,1]
    s = bulidLinkList(nums)
    printLinkList(s)
    
    #获取倒数第n个节点
    testCase_n = [-1,0,1,2,3,4,5,6,7,8,9,10,20]
    testCase_s = [s for i in range(len(testCase_n))]
    
    print(list(map(lambda node: "None" if node == None else node.x, 
                   map(getLastNode, testCase_s, testCase_n))))
    