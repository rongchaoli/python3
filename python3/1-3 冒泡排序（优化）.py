#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336

# 冒泡排序
# 如果已经是一个有序序列，则不需要再排序。
data = [1,2,3,4,5]
def sort(data):
    print('排序前：')
    print(data)
    for i in range(len(data)-1):
        flag = False
        for j in range(len(data)-1-i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                flag = True
        print('第{}次排序后：'.format(i+1))
        print(data)
        if not flag:
            return # 或者break退出循环
sort(data)
print('排序后：')
print(data)