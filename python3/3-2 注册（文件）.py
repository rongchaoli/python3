#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336

# 注册
# 注册信息存放在文件中
infoFile = 'E:/userinfo.txt'  # \\或者/
 
i = 0
for i in range(3):
    flag = True
    username = input('please inupt username:').strip()
    passwd = input('please inupt passwd:')
    confirm_passwd = input('please inupt confirm_passwd:')
    with open(infoFile, 'r') as f:
        # f.seek(0)
        for line in f.readlines():
            user, pwd = line.strip().split(',')
            if user == username:
                print('username is already exist.')
                i += 1
                flag = False               
                break
    if flag == True:   
        if passwd != confirm_passwd:
            print('passwd is unequall.')
            i += 1
        else:
            print('register success.')
            with open(infoFile, 'a') as f2:
                f2.write('\n' + username + ',' + passwd)
            break
else:
    print('over, try next day.')