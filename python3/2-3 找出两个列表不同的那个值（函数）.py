#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336

# 两个列表，其中一个列表比另外一个列表多一个元素，写一个函数，返回这个元素
lia = [1,2,3,4,5,4]
lib = [1,2,3,4,5]
 
def findElement(lia, lib):
    if len(lia)>len(lib):
        for i in lia:
            if i not in lib:
                return i
            else:
                if lia.count(i)>lib.count(i):
                    return i
    else:
        for i in lib:
            if i not in lia:
                return i
            else:
                if lib.count(i)>lia.count(i):
                    return i
 
re = findElement(lia, lib)
print(re)