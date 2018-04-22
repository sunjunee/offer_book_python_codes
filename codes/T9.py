# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-21 18:57:52
"""

#用两个栈实现一个队列

class Stack():
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append(x)
        
    def pop(self):
        return self.stack.pop()
    
    def printStack(self):
        print(self.stack)
    
    def lens(self):
        return len(self.stack)

#用上面的栈实现
class Queue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def push(self, x):
        self.stack1.push(x)
    
    def pop(self):
        if(self.stack2.lens() == 0):
            #将stack1中的数据全部pop然后push到stcak2中
            for i in range(self.stack1.lens()):
                self.stack2.push(self.stack1.pop())
        try:
            return self.stack2.pop()
        except Exception as e:
            print(e)
    
if __name__ == "__main__":
    q = Queue()
    q.push(2)
    q.push(4)
    print(q.pop())
    q.push(3)
    q.push(5)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    