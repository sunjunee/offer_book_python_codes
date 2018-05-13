# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-13 17:01:28
"""

# T41 数据流中的中位数
# 如何得到一个数据流中的中位数？ 如何从数据流中读取出奇数个数值，那么中位数
# 就是所有数值排序设置后位于中间的数值，如果从数据流中读取出偶数个数值，则
# 中位数就是所有数值排序之后中间两个数的平均值

def getMediumNum(nums):
    if(len(nums) == 0):
        return
    elif(len(nums) == 1):
        return nums[0]
    elif(len(nums) == 2):
        return (nums[0] + nums[1]) / 2

    #注意nums是流式接收的
    sortedNums = [min(nums[0], nums[1]), max(nums[0], nums[1])]
    for num in nums[2:]:
        pos = insert(sortedNums, 0, len(sortedNums) - 1, num)
        sortedNums.insert(pos, num)
    
    if(len(sortedNums) % 2):
        return sortedNums[int(len(sortedNums)/2)]
    else:
        return (sortedNums[int(len(sortedNums)/2)] + sortedNums[int(len(sortedNums)/2) - 1]) / 2
        
#假设nums已经从小到大排序好了
def insert(nums, start, end, n):
    if(end - start == 1):
        if(n < nums[start]):
            return start
        elif(n < nums[end]):
            return end
        else:
            return end + 1
    
    center = int((start + end) / 2)
    
    if(nums[center] == n):
        return center
    elif(nums[center] > n):
        return insert(nums, start, center, n)
    else:
        return insert(nums, center, end, n)

if __name__ == "__main__":
    print(getMediumNum([4,3,2,9,1]))