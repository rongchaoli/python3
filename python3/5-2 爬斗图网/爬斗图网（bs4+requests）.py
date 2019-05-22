#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336


import requests
from bs4 import BeautifulSoup

# 获取网页源码
def get_html(url):
    # url = 'http://www.doutula.com/article/list/?page=1'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    request = requests.get(url=url, headers=headers)  # 网址发送get请求
    response = request.content.decode('utf-8')  # 获取源码
    # print(response)
    return response


# 获取每个图片系列的url
def get_img_html(html):
    # soup = BeautifulSoup(html,'html.parser')
    soup = BeautifulSoup(html, 'lxml')  # 创建soup对象，解析网页，比html.parser更强大，更快
    all_a = soup.find_all('a', class_='list-group-item')  # 获取a标签[注意：这里的类名只是a标签中的一个]，如果有class或id来命名，一定要加上名字
    # print(type(all_a)) # <class 'bs4.element.ResultSet'>
    # print(all_a)
    # print(len(all_a))
    for i in all_a:
        # print(i)
        # print(i['href'])
        img_html = get_html(i['href'])  # 获取内页源码，i['href']表示获取a标签的href属性值
        # print(img_html)
        get_img(img_html)  # 一页中的一个系列


# 获取图片系列中每个图片的url
c = 0
def get_img(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='artile_des')
    # find_all后面不能跟find，因为find是找一个，find_all是找多个，从多个中找一个是不对的
    # print(items)
    # print(type(items))  # <class 'bs4.element.ResultSet'>
    imgurl_list = []
    # print(len(items))
    for i in items:
        # print(type(i))  # <class 'bs4.element.Tag'>
        if i.find('img') is not None:
            imgurl = i.find('img')['src']  # img标签下的src属性值
            imgurl_list.append(imgurl)
    print(len(imgurl_list),imgurl_list)

    # global c
    # c +=len(imgurl_list)
    # print(c)

    for i in imgurl_list:
        save_img(i)


# 下载图片
x = 0

def save_img(img_url):
    global x  # 全局变量
    x += 1

    print('正在下载第%s张图片: %s' % (x, img_url))
    img_type = img_url.split('.')[-1]  # 因为图片格式不一样，所以切片，把链接中图片后缀获取到，用于下面拼接文件名
    img_content = requests.get(img_url).content
    import os
    if not os.path.exists('./doutu'):
        os.mkdir('./doutu')
    with open('doutu/%s.%s' % (x, img_type), 'wb')  as f:  # urllib下的retrieve也可以下载
        f.write(img_content)




# 主函数
def main():
    start_url = 'http://www.doutula.com/article/list/?page={}'
    for i in range(6, 7):
        # print(start_url.format(i))
        start_html = get_html(start_url.format(i))
        get_img_html(start_html)  # 获取内页图片的url


if __name__ == '__main__':  # 判断文件入口
    main()
