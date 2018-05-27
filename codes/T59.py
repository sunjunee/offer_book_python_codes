# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 16:57:04
"""

# T59 队列的最大值
# 给定一个数组和滑动窗口的大小，请找出所有
# 滑动窗口里的最大值。例如，如果输入数组
# {2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么
# 存在6个滑动窗口，其最大值依次是{4,4,6,6,6,5}

# 用一个队列来存储当前的最大值
# 对于每一个新来的值，从队尾开始依次和值比较
# 如果队列中的值小于新来的值，则删掉，否则
# 将新来的值加入队列。

def getMaxValue(nums, k):
    queue = [0]
        
    for i in range(1, len(nums)):
        #如果当前队列头元素超出滑动窗口
        if(i - queue[0] == k):   
            queue = queue[1:]
        
        #从queue尾部开始，找到当前值放置的位置，并删掉后面的元素
        for j in range(len(queue)-1, -1, -1):
            if(nums[i] > nums[queue[j]]):
                del queue[j]
        queue.append(i)
        
        #从第k-1个数开始，打印最大值
        if(i >= k - 1):
            print(nums[queue[0]])
        
            
    
    