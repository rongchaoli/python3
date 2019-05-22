#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336


# 一个列表，找出只出现一次的元素

list_a = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
list_b = []
for i in list_a:
    if list_a.count(i) == 1:
        list_b.append(i)
print(list_b)