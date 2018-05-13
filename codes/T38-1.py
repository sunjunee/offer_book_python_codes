# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-13 14:41:51
"""

#T38-1 求一组字符的所有组合。

# 从左到右遍历，每个字符有两种可能,取/不取
# 到最右边，打印已取字符，如果不为空则打印

def getCombination(charList):
    if(len(charList) == 0):
        return
        
    resu = []
    Combination(charList, 0, resu)
    print("\n")
    
def Combination(charList, index, resu):
    if(index == len(charList)):
        if(resu != []):
            print(resu)
        return
    #取
    resu.append(charList[index])
    Combination(charList, index + 1, resu)
    resu.pop()
    #不取
    Combination(charList, index + 1, resu)

if __name__ == "__main__":
    testCase = [[1],
                [1,2,3]]
                
    print(list(map(getCombination, testCase)))