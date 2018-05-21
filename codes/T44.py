# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-16 21:49:41
"""

# T44 数字序列中的某一数字
# 数字以01234567891011...的格式序列化到一个字符串序列中，在这个序列中，
# 第5位是5，第13位是1...请写一个函数，求任意第n位的数字。

def getDigit(index):
    pre, cur = 0, 1
    digits = 0
    while(digits + (10 ** cur - 10 ** pre) * cur < index):
        digits += (10 ** cur - 10 ** pre) * cur
        pre, cur = cur, cur + 1
    
    tem1 = (index - digits) // cur
    tem2 = (index - digits) % cur

    if(tem2 == 0):  return int(str(10 ** pre + tem1 - 1)[-1])
    return int(str(10 ** pre + tem1)[tem2 - 1])
    
    