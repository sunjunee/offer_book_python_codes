# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 11:33:51
"""

#位运算:二进制中1的个数(不要尝试去移动数字，因为可能是复负数)
#把一个整数减去1然后与之作与运算，就去掉了最右边的一个1

def countOneNum(n):
    num = 0
    
    while(n):
        n = n & (n - 1)
        num += 1
    
    return num

if __name__ == "__main__":
    testCase = [0, 1, 2, 3, 4, 5, 6]
    print(list(map(lambda x : bin(x), testCase)))
    print(list(map(countOneNum, testCase)))