# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-01 11:10:59
"""

#包含min函数的栈，在栈中实现一个能够获得栈的最小元素的min函数，
#使得min、push、pop的时间复杂度都是O(1)

class newStack():
    def __init__(self):
        self.dataStack = []
        self.minStack = []  #维护一个minSatck，用于保存当前栈顶元素及以下的最小值
    
    def min(self):
        if(self.minStack != []):
            return self.minStack[-1]
    
    def push(self, v):
        self.dataStack.append(v)
        if(self.minStack == []):
            self.minStack.append(v)
        elif(v <= self.minStack[-1]):
            self.minStack.append(v)
    
    def pop(self):
        if(self.dataStack != []):
            v = self.dataStack.pop()
            if(v == self.minStack[-1]):
                self.minStack.pop()
            
            return v
        
if __name__ == "__main__":
    stack = newStack()
    stack.push(0)
    print(stack.min())
    stack.push(1)
    print(stack.min())    
    stack.push(-5)
    print(stack.min())
    stack.push(10)
    print(stack.min())
    stack.push(5)    
    print(stack.min())
    stack.push(-20)    
    print(stack.min())
    stack.pop()    
    print(stack.min()) 