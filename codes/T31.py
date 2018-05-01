# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-01 11:26:52
"""

#栈的压入弹出序列
#输入两个整数序列，第一个序列是栈的压入顺序，第二个是栈的弹出顺序，
#判断第二个序列是否正确，假设序列中的元素都不重复。

def judgePushPop(push, pop):
    if(push == [] or pop == []):    return False
    
    if(len(push) != len(pop)):  return False  
    
    stack = []
    
    i = 0
    for p in push:
        stack.append(p)
        
        while(len(stack) > 0 and pop[i] == stack[-1]):
            stack.pop()
            i += 1
    
    return True if len(stack) == 0 else False
    

        

print(judgePushPop([1,2,3,4,5], [4,5,3,2,1]))