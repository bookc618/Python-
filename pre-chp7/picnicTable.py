#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 
'''
打印表格式数据,用 rjust()、ljust()和 center()方法对齐文本,用 strip()、rstrip()和 lstrip()删除空白字符

'''
def printPicnic(itemdict, leftwidth, rightwidt):
    print('PICNIC ITEMS'.center(leftwidth + rightwidt, '-'))
    for k, v in itemdict.items():
        print(k.ljust(leftwidth, '.') + str(v).rjust(rightwidt))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
