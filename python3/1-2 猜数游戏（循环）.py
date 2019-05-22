#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336



# 猜数游戏
# 猜对，打印猜对信息，退出程序
# 最多连续猜三次，连续错三次后询问是否继续玩游戏，是，继续猜，否，退出程序

luck_num = 19
n = 3
while n > 0:
    guess_nu = int(input("your guess:"))
    if guess_nu > luck_num:
        print('your guess bigger.')
    elif guess_nu < luck_num:
        print('your guess smaller.')
    else:
        print('恭喜您，猜对了。')
        break
    n -= 1  # 减号和等号之间不能有空格
    if n > 0:
        print('{} times left.'.format(n))
    if n==0:
        choose = input('失败次数过多，是否继续游戏？（是y）：')
        if choose.lower()=='y':
            n = 3
        else:
            exit('退出了。')