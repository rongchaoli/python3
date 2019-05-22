#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336



# 模拟登陆、锁定用户
#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# Author:wengy
'''
dic = {
    "sc":{
        "cd":['xd', 'jn', 'ch'],
        "my":['yx', 'zt', 'xx']
    },
    "gd":{
        "gz":['gz1', 'gz2', 'gz3'],
        "zs":['zs1', 'zs2', 'zs3']
    }
}

ret = dic.keys()
print(ret)
ret = dic['sc'].keys()
print(ret)
ret = dic['sc']['cd']
print(ret)
'''

import sys
account_file = 'F:\match.txt'
locked_file = 'F:\locked.txt'

def deny_account(username):
    print('locked.')
    with open(locked_file, 'a') as deny_f:
        deny_f.write('\n' +username)
def main():
    retry_count = 0
    retry_limit = 3
    while retry_count < retry_limit:
        flag = False
        username = input('input your name:')
        if len(username) == 0:
            print('username is null')
            continue
        with open(locked_file, 'r') as lock_f:
            '''
            另外一种用户名匹配方式
            lines = []
            for line in lock_f.readlines():
                lines.append(line.strip())
            if username in lines:
            '''
            for line in lock_f.readlines():
                if len(line) == 0:
                    continue
                if username == line.strip():
                    sys.exit('user:{} locked.'.format(username))
        '''
        if len(username) == 0:
            print('username is null')
            continue
        '''
        password = input('passwd:')
        with open(account_file, 'r') as account_f:
            # flag = False
            for line in account_f.readlines():
                user, pwd = line.strip().split() # strip是去换行符？
                if username == user and password == pwd:
                    print('login success')
                    flag = True
                    break
        if flag == False:
            if retry_count < 2:
                print('username or password is not correct.')
            retry_count += 1
        else:
            break
    else:
        deny_account(username)

if __name__ == '__main__':
    main()