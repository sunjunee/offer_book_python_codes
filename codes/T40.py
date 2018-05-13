# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-13 15:59:33
"""

# T40 最小的k个数
# 输入n个整数，找出其中最小的k个整数

# 维护一个排序数组，从小到大放k个数，
# 初始化为n个中的前k个，然后依次将后续的
# n-k个进行插入操作。

def getMinKNums(nums, k):
    lens = len(nums)
    if(k >= lens):
        return nums
        
    resu = nums[0:k]
    resu = sorted(resu)
    
    for n in nums[k:]:
        pos = insert(resu, 0, k-1, n)
        print(n, pos)
        resu.insert(pos, n)
        del resu[k]
        
    return resu 

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
    testCase_nums = [[2,3,4,8,9,10],
                     [2,3,4],
                     [6,5,4,2,9]]
    testCase_k = [3,3,3]

    print(list(map(getMinKNums, testCase_nums, testCase_k)))