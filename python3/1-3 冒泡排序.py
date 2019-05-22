#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336


# 冒泡排序
data = [10, 4, 33, 21, 54, 8, 11, 5]
def sort(data):
    print('排序前：')
    print(data)
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
        print('第{}次排序后：'.format(i+1))
        print(data)
sort(data)
print('排序后：')
print(data)

# 排序前：
# [10, 4, 33, 21, 54, 8, 11, 5]
# 第1次排序后：
# [4, 10, 21, 33, 8, 11, 5, 54]
# 第2次排序后：
# [4, 10, 21, 8, 11, 5, 33, 54]
# 第3次排序后：
# [4, 10, 8, 11, 5, 21, 33, 54]
# 第4次排序后：
# [4, 8, 10, 5, 11, 21, 33, 54]
# 第5次排序后：
# [4, 8, 5, 10, 11, 21, 33, 54]
# 第6次排序后：
# [4, 5, 8, 10, 11, 21, 33, 54]
# 第7次排序后：
# [4, 5, 8, 10, 11, 21, 33, 54]
# 排序后：
# [4, 5, 8, 10, 11, 21, 33, 54]