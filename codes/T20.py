# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 15:03:02
"""

#表示数值的字符串：实现一个函数来判断一个字符串是否表示数值
#如+100, 5e2, -123, 3.1415, -1e-16
#{+-}{digits}.{digits}[eE]{+-}{digits} 

def judgeString(string):
    pA = pB = pC = True
    
    index, pA = getInteger(string, 0)
    
    if(index <= len(string) - 1 and string[index] == "."):
        index, pB = getUsignInteger(string, index + 1)
    
    if(index <= len(string) - 1 and (string[index] == "e" or string[index] == "E")):
        index, pC = getInteger(string, index + 1)
    
    if(pA and pB and pC and index == len(string)):
        return True

    return False
                
 
def getUsignInteger(string, index):
    p = index
    pA = False
    while(p <= len(string) - 1 and string[p] >= '0' and string[p] <= '9'):
        p += 1
    
    if(p > index):
        pA = True
    
    return p, pA

def getInteger(string, index):    
    if(string[index] == '-' or string[index] == "+"):
        index += 1
    
    return getUsignInteger(string, index)


if __name__ == "__main__":
    testCase = ["+100", "5e2", "-123", "3.145678", "-12.56e+23",
                "-0.13e.w", ".e2", "+", "-.23", "5e0.2"]
    
    print(list(map(judgeString, testCase)))