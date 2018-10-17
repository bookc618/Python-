#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 

PASSWD_LIST = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
               'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
               'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print("Usage: py 密码保管箱.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in PASSWD_LIST:
    pyperclip.copy(PASSWD_LIST[account])
    print(account + " 的密码已复制到剪粘板!")
else:
    print("未找到 " + account + " 的密码！是否选择添加到数据库？Y是/[n]否： ")
    ans = input()
    if ans == 'n':
        sys.exit()
    elif ans == 'Y' or ans == 'y':
        print("请输入密码串:")
        pwdinfo = input()
        PASSWD_LIST[account] = pwdinfo
        print("您已添加名称为 " + account + " 的密码串，密码是： " + PASSWD_LIST[account])
    else:
        print("请输入正确的提示字符！")
