# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-21 20:45:24
"""

# T46 把数字翻译成字符串
# 给定一个数字，我们按照如下规则把它翻译成字符串：
# 0翻译成a，1翻译成b...11翻译成l...25翻译成z。
# 一个数字可能有多个翻译，例如12258有5中不同的翻译
# 如：bccfi、bwfi、bczi、mcfi、mzi

# 思路： 递归进行计算，每次移动一步，或者两步
#       判断是否能组成字母，不能则返回

def getTranfrom(num):
    return trans(str(num), 0, "")

def getChar(num):
    return chr(ord("a") + int(num))
    
def trans(num, i, strs):
    if(i == len(num)):
        return 1
    else:
        n = 0
        if(i < len(num)):
            n += trans(num, i + 1, strs + getChar(int(num[i])))
        if(i < len(num) - 1 and int(num[i:i+2]) <= 25 and num[i] != '0'):
            n += trans(num, i + 2, strs + getChar(int(num[i:i+2])))
        return n

if __name__ == "__main__":
    print(getTranfrom(12258))