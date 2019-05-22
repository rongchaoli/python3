#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336


# 列表 [11,22,33,44,55,66,77,88,99]，
# 将所有大于 66 的值保存至字典的第一个key中，
# 将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
l= [11,22,33,44,55,66,77,88,99]
bignum=[]
smallnum=[]
dir={}
for num in l:
    if num>66:
        bignum.append(num)
    if num<66:
        smallnum.append(num)
    else:
        pass
dir['k1']=bignum
dir['k2']=smallnum
print(dir)