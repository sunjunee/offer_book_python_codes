# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 13:27:41
"""

#打印1到n位的最大数字
def printNum(n, prefix, i):
    if(i == n):
        print(prefix.lstrip("0"),end = " ")
    else:
        for t in range(10):
            printNum(n, prefix + str(t), i + 1)

def getResu(n):
    printNum(n, "", 0)
    print("\n")

if __name__ == "__main__":
    testCase = [1, 2, 3, 4]
    list(map(getResu, testCase))