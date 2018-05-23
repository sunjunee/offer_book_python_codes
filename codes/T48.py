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

# 类似动态规划的思想，如果下一个值在当前的子串中，则修改子串；
# 否则子串长度加一。继续考虑下一个值 

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
        dicts[c] = 1
        j += 1
        

    return maxLens

def getIndex(s):
    return ord(s) - ord("a")

# 更佳解法：
# 考虑以某个字符结尾的子串长度，对于某字符，
# 记录之前每一个字符的最新出现的位置，如果
# 当前字符没有出现过，则子串加一；如果出现过，
# 则考虑其位置，如果在子串开头之前，则子串加一
# 否则子串从与其重复的字符的位置的后一个位置
# 开始。

def getMaxSubLen(strs):
    lens = len(strs)
    posDicts = {}
    
    i, maxLen = 0, 0
    for j in range(lens):
        if(strs[j] in posDicts.keys()):
            pos = posDicts[strs[j]]
            if(pos >= i):
                i = pos + 1
                continue
        posDicts[strs[j]] = j
        
        if(j - i + 1 > maxLen):
            maxLen = j - i + 1
    return maxLen
        
if __name__ == "__main__":
    print(getMaxSubLen("abccafd"))