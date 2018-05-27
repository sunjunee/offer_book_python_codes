# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 16:50:18
"""

# T58-2 左旋转字符串
# 字符串的左旋转操作是把字符串前面的若干
# 字符转移到字符串的尾部。比如输入字符串
# "abcdefg"和数字2，该函数将返回左旋转
# 两位得到的结果"cdefgab"

def rotateStrs(strs, index):
    return strs[index:] + strs[0:index]

print(rotateStrs("abcdefg", 2))