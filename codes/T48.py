# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-21 22:06:42
"""

# T48 最长不含重复字符的子字符串
# 请从字符串中找到一个最长的不包含重复字符的子字符串
# 计算该最长子字符串的长度。假设字符串中只包含a-z的字符。
# 例如：arabcacfr中最长的不含重复字符的子字符串是acfr，长度为4

def getLongestSubStr(strs):
    lens = len(strs)
    i, j = 0, 0
    dicts = [0 for i in range(26)]
    maxLens = 1
    while(j < lens):
        c = getIndex(strs[j])
        if(dicts[c]):
            while(strs[i] != strs[j]):
                dicts[getIndex(strs[i])] = 0
                i += 1
            dicts[getIndex(strs[i])] = 0
            i += 1
        
        if(j - i + 1 > maxLens):
            maxLens = j - i + 1        
        j += 1
        dicts[c] = 1

    return maxLens

def getIndex(s):
    return ord(s) - ord("a")

if __name__ == "__main__":
    print(getLongestSubStr("arabcacfr"))