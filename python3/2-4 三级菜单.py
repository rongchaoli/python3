#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336


# 三级菜单

# 　　可依次选择进入各子菜单

# 　　可从任意一层往回退到上一层

# 　　可从任意一层退出程序


# si = {
#     '四川':{
#         '成都':{
#             '新都':['三河街道', '大丰街道', '石板滩镇'],
#             '金牛':['金泉街道', '抚琴街道', '茶店子街道', '沙河源街道'],
#             '双流':['东升街道', '中和街道', '西航港街道', '华阳镇街道']
#         },
#         '绵阳': {
#             '游仙': ['小枧沟镇', '忠兴镇', '富乐街道'],
#             '涪城': ['创业园街道', '塘汛街道', '工区街道', '丰谷镇']
#         }
#     },
#     '云南': {
#         '昆明市': {
#             '五华区': ['龙翔街道', '丰宁街道', '莲华街道'],
#             '盘龙区': ['青云街道', '松华街道']
#         },
#         '玉溪市': {
#             '红塔区': ['大营街镇', '高仓镇', '研和镇'],
#             '江川区': ['大街镇', '江城镇']
#         }
#     }
# }

print('欢迎使用行政区域查询系统：'.center(30, '*'))

while True:
    for i in si:
        print(i)
    pro = input('请输入省(q退出)：')
    if pro in si:
        # for i in si[pro]:
        #     print('\t{}'.format(i))
        while True:
            for i in si[pro]:
                print('\t{}'.format(i))
            city = input('\t请输入市(r上一级，q退出)：')
            if city in si[pro]:
                # for i in si[pro][city]:
                #     print('\t\t{}'.format(i))
                while True:
                    for i in si[pro][city]:
                        print('\t\t{}'.format(i))
                    dis = input('\t\t请输入区县(r上一级，q退出)：')
                    if dis in si[pro][city]:
                        for i in si[pro][city][dis]:
                            print('\t\t\t{}'.format(i))
                        choise = input('\t\t已到最后一层（r上一级，q退出）：')
                        if choise.strip().lower()=='q':
                            exit()
                        elif choise.strip().lower()=='r':
                            pass
                    elif dis.strip().lower()=='q':
                        print('谢谢使用，再见！')
                        exit()
                    elif dis.strip().lower()=='r':
                        break
            elif city.strip().lower() == 'q':
                print('谢谢使用，再见！')
                exit()
            elif city.strip().lower() == 'r':
                break
    elif pro.strip().lower() == 'q':
        print('谢谢使用，再见！')
        exit()