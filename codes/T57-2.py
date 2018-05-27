# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 16:07:01
"""

# T57-2 和为s的连续正数序列
# 输入一个整数s，打印出所有和为s的连续正数
# 序列，例如输入15，由于1+2+3+4+5=4+5+6=
# 7+8=15，所有打印出3个连续的序列

def getContinueSeqs(s):
    if(s < 3):  return
    
    i, j = 1, 2
    end = s // 2 + 1
    sums = 3
    while(i <= end):   
        if(sums == s):
            print(list(range(i, j+1)))
        while(sums > s and i <= end):
            sums -= i
            i += 1
            if(sums == s):
                print(list(range(i, j+1)))
                
        j += 1
        sums += j
        
getContinueSeqs(15)