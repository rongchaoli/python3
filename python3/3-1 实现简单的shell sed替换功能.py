#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336

# 实现简单的shell sed替换功能
import sys
f = open('yesterday', 'r', encoding='utf-8')
f2 = open('yesterday_bak.txt', 'w', encoding='utf-8')

find_str = sys.argv[1]
replace_str = sys.argv[2]
for line in f:
    if find_str in line:
        line = line.replace(find_str, replace_str)
    f2.write(line)
f.close()
f2.close()