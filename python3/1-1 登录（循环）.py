#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336


# 如果登录成功，输出欢迎信息，退出程序
# 如果错误次数3次，退出程序

#用while来写
count =0  # 定义一个计数器
while count <3:
    username = input('please enter your username:')
    passwd = input('please enter your password:')
    if username.strip()=='':
        print('username is not null...')
    elif username == 'jack' and passwd == '123456':
        print('welcome, %s' %username)
        break
    else:
        print('username or password error...')
    count+=1
else:
    print('失败次数过多，请稍后再试！')