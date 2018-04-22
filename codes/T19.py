# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 14:08:17
"""

#正则表达式匹配： *： 前面字符重复0次及以上， .匹配任意字符
#有点复杂，主要考虑后面是否有*，如果有，多种情况可能出现，1）
#前面能匹配上，则考虑下一个字母，正则移动两位或者不移动，2）
#前面不能匹配上，则认为*是0，字母不动，正则后移2。3）

def MatchReg(string, regs, i, j):
    if(i == len(string) and j == len(regs)):
        return True
    
    if(i < len(string) and j == len(regs)):
        return False
        
    if(j + 1 < len(regs) and regs[j + 1] == "*"):
        if(regs[j] == string[i] or regs[j] == "."):
            return (MatchReg(string, regs, i + 1, j + 2) or 
                    MatchReg(string, regs, i + 1, j) or
                    MatchReg(string, regs, i, j + 2))
        else:
            return MatchReg(string, regs, i, j + 2)

    if((i < len(string) and regs[j] == string[i])
        or regs[j] == '.'):
        
        return MatchReg(string, regs, i + 1, j + 1)
    
    return False

def Match(string, regs):
    return MatchReg(string, regs, 0, 0)
    
if __name__ == "__main__":
    testCase_string = ['aaa', 'aaa', 'aaa', 'aaa']
    testCase_regs = ['a.a', 'ab*ac*a', 'aa.a', 'ab*a']
    
    print(list(map(Match, testCase_string, testCase_regs)))
            
    
