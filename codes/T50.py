# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-23 09:25:11
"""

# T50 第一个值出现一次的字符
# 在字符串中找到第一个只出现一次的字符。
# 例如输入“abaccdeff”中第一个只出现一次的字符是b

# 两步走： 1、使用字典存储字符及其次数
#        2、遍历字符串找第一个只出现一次的字符

def getFirstOnce(strs):
    if(len(strs) == 0): return None
    
    dicts = {}
    for s in strs:
        if(s not in dicts.keys()):
            dicts[s] = 1
        else:
            dicts[s] = dicts[s] + 1
    
    for s in strs:
        if(dicts[s] == 1):
            return s
    
    return None

print(getFirstOnce("abavbcvaaaaaavcvd"))