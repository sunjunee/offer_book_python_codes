# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-21 19:55:51
"""

#求斐波拉契数列第n项: 生兔子问题，切绳子问题，爬台阶问题
#动态规划，不要用递归 -- 用循环来求解

def getFibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        fabon = [0, 1]
        for i in range(2, n + 1):
            fabon[0], fabon[1] = fabon[1], sum(fabon)
        return fabon[1]

if __name__ == "__main__":
    n = [0,1,2,3,4,5,6,7,8,100]
    
    print(list(map(getFibonacci, n)))