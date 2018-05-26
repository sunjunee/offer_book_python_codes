# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-26 19:47:16
"""

# 面试题52：两个链表的第一个公共结点
# 题目：输入两个链表，找出它们的第一个公共结点。

# 先确定两个链表长度
# 公共部分是等长的，则让长的先遍历到后续长度和短的相等
# 然后一起遍历

class ListNode():
    def __init__(self, x):
        self.x = x
        self.next = None

def FindCommonFirstNode(s1, s2):
    len1 = getLens(s1)
    len2 = getLens(s2)
    
    if(len1 > len2):
        s1, s2, len1, len2 = s2, s1, len2, len1
    
    for i in range(len2 - len1):
        s2 = s2.next
    
    while(s1.x != s2.x):
        s1, s2 = s1.next, s2.next
    
    return s1.x
    
def getLens(s):
    lens = 0
    while(s):
        s = s.next
        lens += 1
    return lens
 
def printLinkList(s):
    while(s):
        print(str(s.x), end = '')
        s = s.next
        if(s):
            print(" -> ", end = '')
    print()
   
if __name__ == "__main__":
    s1 = p = ListNode(0)
    p.next = ListNode(1); p = p.next
    p.next = ListNode(2); p = p.next; cur = p
    p.next = ListNode(3); p = p.next
    p.next = ListNode(4); p = p.next
    
    s2 = p = ListNode(0)
    p.next = ListNode(1); p = p.next
    p.next = ListNode(2); p = p.next
    p.next = ListNode(3); p = p.next
    p.next = cur
    
    #      0 -> 1 -> 2 -> 3 -> 4 
    #                ^
    #                |   
    # 0 -> 1 -> 2 -> 3
    printLinkList(s1)
    printLinkList(s2)
    
    print(FindCommonFirstNode(s1, s2))

