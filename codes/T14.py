# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 11:09:10
"""

#动态规划减绳子： 长度为n的绳子，最少剪成两段，每段最短为1
#f(n) = max{f(n-i) * f(i)}

def getMaxCut(l):
    if(l == 1):
        return 0
    elif(l == 2):
        return 1
    elif(l == 3):
        return 2
    else:
        fn = [0, 1, 2, 3]
        
        for n in range(4, l + 1):
            tem = 0
            for i in range(1, n):
                if(fn[i] * fn[n - i] > tem):
                    tem = fn[i] * fn[n - i]
            fn.append(tem)
        
        return fn[-1]

if __name__ == "__main__":
    testCase = [1,2,3,4,5,6,7,8,9,10]
    
    print(list(map(getMaxCut, testCase)))