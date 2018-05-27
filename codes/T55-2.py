# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 14:34:01
"""

# T55-2 判断一棵树是不是二叉平衡数
# 二叉平衡树的任意节点的左右子树稍深度
# 相差不超过1，那么它就是一颗二叉平衡树

# 实际上可以递归来判断，分别计算左右子树的
# 深度，然后判断差值是否小于1，同时返回新的
# 深度。

def judgeBalanceTree(root):
    resu, _ = judge(root)
    return resu
    
def judge(root):
    if(root == None):   return True, 0
    
    left_resu, left_depth = judge(root.left)
    right_resu, right_depth = judge(root.right)
    
    if(left_resu and right_resu and abs(left_depth - right_depth) <= 1):
        return True, 1 + max(left_depth, right_depth)
    else:
        return False, 1 + max(left_depth, right_depth)
        
