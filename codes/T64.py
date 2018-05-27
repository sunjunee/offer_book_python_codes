# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 21:06:19
"""

# T64 求1+2+...+n
# 求1到n的和，要求不适用乘除法、for、while
# if、else、switch、case等关键词及条件判断
# 语句(A?B:C)

n = 1
s = 0
class Accuramuate():
    def __init__(self):
        global s, n        
        s += n
        n += 1