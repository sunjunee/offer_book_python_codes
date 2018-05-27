# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-27 16:36:21
"""

# T58 翻转字符串
# 输入一个英文句子，翻转句子中单词的顺序，但是单词内
# 字符的顺序不变，为简单起见，标点符号和普通字母一样
# 处理，例如输入字符串“I am a student.” 则输出为：
# "student. a am I"

def TransStrs(strs):
    strs = strs.split(' ')
    return ' '.join(strs[::-1])

print(TransStrs("I am a student."))