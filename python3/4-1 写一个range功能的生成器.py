#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336


# 写一个range功能的生成器
# 
def rangeX(n):
    count = 0
    while count < n:
        # print(count)
        yield count
        count +=1
    return 'done'

f = rangeX(3)
print(f)
for i in f:
    print(i)

'''
<generator object rangeX at 0x00000000021EE8E0>
0
1
2
'''