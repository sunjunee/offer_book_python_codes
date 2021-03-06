# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-14 08:45:46
"""

# T43 1~n整数中1出现的次数
# 求1~n这n个整数的十进制表示中1出现的次数。
# 例如输入12，则这些整数中包含数字1的有
# 1、10、11、12

# 思路：对于数字21345,1到21345中1出现的次数的计算，可以如下计算：
# （1） 考虑1346 - 21345： 最高位出现1的次数是10 ^ 4 + 1346
#                         其他位出现的次数是2 * 4 * 10 ^ 3
#  (2)  考虑1 - 1345：  分为346 - 1345和1 - 345两部分

def getNumOfDigitOne(num):
    if(num // 10 == 0):
        if(num == 0):
            return 0
        else:
            return 1
    
    strs = str(num)[1:].lstrip("0")
    preNum = 0 if strs == '' else eval(strs)
    
    #计算preNum + 1到Num
    high = int(str(num)[0])
    digitNum = len(str(num)) - 1
    
    if(high == 1):
        now = preNum + 1 + high * digitNum * (10 ** (digitNum - 1))
    else:
        now = 10 ** digitNum + high * digitNum * (10 ** (digitNum - 1))

    return now + getNumOfDigitOne(preNum)
    
print(getNumOfDigitOne(21345))            
    