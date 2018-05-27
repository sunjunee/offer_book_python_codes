# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 20:02:54
"""

# T61 扑克牌中的顺子
# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是
# 连续的。2-10为数字本身，J、Q、K分别是11,12,13，A是1，大小王
# 可以是任意数字

# 即现将数字排序（除大王小王），
# 如果有重复的数字牌，则不是顺子
# 1、如果相邻之差减一的和等于0,则是顺子
# 2、如果相邻之差减一的和等于1，且至少有一张王，则是顺子
# 3、如果相邻之差减一的和等于2，且有两张王，则是顺子
# 否则不是顺子

def judgePokers(pokers):
    # 0代表王，其实扑克是1-13的数字
    pokers.sort()
    
    numOfJoker = 0  # 王的个数
    for p in pokers:
        if(p == 0):
            numOfJoker += 1
    
    diff = 0
    for i in range(numOfJoker, len(pokers)-1):
        if(pokers[i] == pokers[i+1]):
            return False
        
        diff += pokers[i+1] - pokers[i] - 1
    
    #判断
    if(diff == 0):
        return True
    elif(diff == 1 and numOfJoker >= 1):
        return True
    elif(diff == 2 and numOfJoker == 2):
        return True
    else:
        return False
    

print(judgePokers([0,0,1,3,4,6]))