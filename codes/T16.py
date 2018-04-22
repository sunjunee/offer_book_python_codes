# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-22 11:50:36
"""

#实现计算数值的整数次方： double Power(double base, int exponent)

def power(base, exponent):
    if(base == 0 and exponent < 0):
        return 0

    e = abs(exponent)
    p = 1.0    
    for i in range(e):
        p *= base
    
    if(exponent < 0):
        p = - p
        
    return p
    
if __name__ == "__main__":
    testCase_base = [1.0, 2.0, 3.5, 0]
    testCase_expo = [0, 2, 4, -5]
    
    print(list(map(power, testCase_base, testCase_expo)))