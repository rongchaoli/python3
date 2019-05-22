#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336


import requests

# 获取页源码
def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    '''
    后台通常会通过此字段判断用户设备类型、系统以及浏览器的型号版本。
    有些编程语言包里网络请求会自定义User-Agent，可以被辨别出来，爬虫中可以设置为浏览器的ua
    '''
    request = requests.get(url=url, headers=headers)  # 发送get请求
    # print(request.status_code)
    response = request.content.decode('utf-8')  # 获取源码
    return response

res = get_html('http://www.doutula.com/article/list/?page=2')
print(res)
