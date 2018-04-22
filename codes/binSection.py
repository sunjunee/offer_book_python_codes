# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-21 11:39:06
"""

import math

#二分查找

def biSection(X, num):
    lens = len(X)
    start = 0
    end = lens - 1
    
    while(start <= end):
        middle = math.floor((start + end) / 2)
        print(middle)
        if(X[middle] != num):
            if(num > X[middle]):
                start = middle + 1
            else:
                end = middle - 1
        else:
            return middle

if __name__ == "__main__":
    testCase = ([0,1,1,4,5,8,9], 8)
    
    print(biSection(*testCase))