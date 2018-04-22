# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-21 19:31:55
"""

#使用两个队列来实现栈
class Queue():
    def __init__(self):
        self.queue = []
    
    def pop(self):
        if(len(self.queue) > 0):
            tem = self.queue[0]
            del self.queue[0]
            return tem
    
    def push(self, x):
        self.queue.append(x)
    
    def getLens(self):
        return len(self.queue)

#用上面的栈结构来构建队列
class Stack():
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    
    def push(self, x):
        #将数据压入到不为空的队列中
        if(self.queue1.getLens() > 0):
            self.queue1.push(x)
        else:
            self.queue2.push(x)
        
    def pop(self):
        #将有数据的队列中的数据，压入另一个队列，只留一个
        if(self.queue1.getLens() > 0):
            for i in range(self.queue1.getLens() - 1):
                self.queue2.push(self.queue1.pop())
            return self.queue1.pop()
        else:
            for i in range(self.queue2.getLens() - 1):
                self.queue1.push(self.queue2.pop())
            return self.queue2.pop()
            
if __name__ == "__main__":
    q = Stack()
    q.push(2)
    q.push(4)
    print(q.pop())
    q.push(3)
    q.push(5)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
