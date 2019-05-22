#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336


import requests
from lxml import etree


# 获取网页源码
def get_html(url):
    # url = 'http://www.doutula.com/article/list/?page=1'
    # 反爬，模拟浏览器访问，用户代理池信息
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    request = requests.get(url=url, headers=headers) # 网址发送get请求，request.status_code是状态码
    response = request.content.decode('utf-8') # 获取源码
    # print(response)
    return response

# 获取每个图片系列的url
def get_img_html(html):
    # print(html)
    soup = etree.HTML(html)
    # items = soup.xpath('//a[@class="list-group-item"]')  # 这样写，items是空，有些a标签有2个类名，有些有3个类名
    items = soup.xpath('//a[contains(@class, "list-group-item")]')

    # print(len(items),items)
    for i in items:
        # print(i)
        img_html = i.xpath('@href')
        # print(img_html)
        img_html = get_html(img_html[0]) # 获取内页源码，i['href']表示获取a标签的href属性值
        get_img(img_html)  # 一页中的一个系列


# 获取图片系列中每个图片的url
def get_img(html):
    soup = etree.HTML(html) # 初始化源码
    items = soup.xpath('//div[@class="artile_des"]') # //表示某个目录下,从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
    # @表示选取属性值
    # []表示过滤条件

    # XPath = '//*[@id="j-nav-menu-container"]/div/div/div/div/div/div[2]/div[1]/a/@href'
    # 获得a标签的href
    #
    # XPath = '//*[@id="j-nav-menu-container"]/div/div/div/div/div/div[2]/div[1]/a/text()'
    # 获得a标签内容

    # print(items)
    # print(type(items))  # <class 'list'>

    for item in items:
        imgurl_list = item.xpath('table/tbody/tr/td/a/img/@src')
        # print(imgurl_list)
        save_img(imgurl_list[0])


# 下载图片
x = 0
def save_img(img_url):
    # print(img_url)
    global x # 全局变量
    x +=1
    print('正在下载第%s张图片: %s'%(x, img_url))
    img_type = img_url.split('.')[-1]
    img_content = requests.get(img_url).content
    with open('doutu/%s.%s'%(x,img_type), 'wb')  as f:  # urllib下的retrieve也可以下载
        f.write(img_content)


# 主函数
def main():
    start_url = 'http://www.doutula.com/article/list/?page={}'
    for i in range(6,7):
        # print(start_url.format(i))
        start_html = get_html(start_url.format(i))
        get_img_html(start_html) # 获取内页图片的url

if __name__ == '__main__':  # 判断文件入口
    main()
