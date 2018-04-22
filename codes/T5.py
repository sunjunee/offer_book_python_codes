# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-04-21 14:33:59
"""

#替换空格，把字符串中的每个空格替换成“%20”

def replaceSpace(S):
    S = S.replace(" ", "%20")
    return S

if __name__ == "__main__":
    testCases = ["I love Yzy.", 
                 "Just do it!",
                 "Oh my god!"]
                 
    print(list(map(replaceSpace, testCases)))