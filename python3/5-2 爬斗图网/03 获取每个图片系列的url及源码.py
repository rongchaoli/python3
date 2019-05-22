#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336


import requests
from bs4 import BeautifulSoup

# 获取页源码
def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    request = requests.get(url=url, headers=headers)  # 发送get请求
    # print(request.status_code)
    response = request.content.decode('utf-8')  # 获取源码
    return response


# 获取每个图片系列的url
def get_img_html(html):
    # soup = BeautifulSoup(html,'html.parser')
    soup = BeautifulSoup(html, 'lxml')
    all_a = soup.find_all('a', class_='list-group-item')
    # print(type(all_a)) # <class 'bs4.element.ResultSet'>
    # print(all_a)
    print(len(all_a))
    for i in all_a:
        # print(i)
        print(i['href'])
        img_html = get_html(i['href'])  # 获取内页源码，i['href']表示获取a标签的href属性值
        # print(img_html)
        # get_img(img_html)  # 一页中的一个系列

res = get_html('http://www.doutula.com/article/list/?page=6')
# print(res)
get_img_html(res)  # 获取内页图片的url
