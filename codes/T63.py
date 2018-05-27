# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 20:53:08
"""

# T63 股票的最大利润
# 假设把某股票的价格按照时间先后顺序存储
# 在数组中，请问买卖该股票一次可能获得的
# 最大利润是多少？ 例如，一只股票在某些
# 时间节点的价格为{9,11,8,5,7,12,16,12}，
# 如果我们能在价格为5的时候买入，并在价格
# 为16的时候卖出，则能获得最大收益11

# 实际上就是求后一数字减去前一数字的最大值。
# 动态规划问题：对于第n个价格，已知前n-1个数字
# 的最大利润和最低价格，如果pn - pmin > maxProfile
# 则更新最大利润，如果pn < pmin，则pmin = pn

def getMaximumProfile(prices):
    lens = len(prices)
    
    if(lens < 2):   return None

    maxProfile = prices[1] - prices[0]
    minPrice = min(prices[0], prices[1])
    
    for i in range(2, lens):
        if(prices[i] - minPrice > maxProfile):
            maxProfile = prices[i] - minPrice
        if(prices[i] < minPrice):
            minPrice = prices[i]
    
    return maxProfile

print(getMaximumProfile([9,11,8,5,7,12,16,12]))
    