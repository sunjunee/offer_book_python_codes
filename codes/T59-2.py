# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 18:58:41
"""

# T59-1: 队列中的最大值
# 请定义一个队列并实现函数max从队列中获取队列的最大值
# 要求函数max、push、pop的时间复杂度都是O(1)

class queue():
    def __init__(self):
        self.queue = []
        self.maxVals = []

    def max(self):
        if(self.maxVals != []):
            return self.maxVals[0]

    def push(self, x):
        for i in range(len(self.maxVals) - 1, -1, -1):
            if(self.maxVals[i] >= x):
                break
            del self.maxVals[i]
        self.maxVals.append(x)
        self.queue.append(x)
    
    def pop(self):
        if(self.queue != []):
            x = self.queue[0]
            del self.queue[0]
            if(x == self.maxVals[0]):
                del self.maxVals[0]
            return x

q = queue()
q.push(0)
print(q.max())
q.push(6)
print(q.max())
q.push(2)
print(q.max())
q.push(10)
print(q.max())
q.push(4)
print(q.max())
q.pop()
print(q.max())
q.pop()
print(q.max())
q.pop()
print(q.max())
q.pop()
print(q.max())
q.pop()
print(q.max())