#!/usr/bin/python3
# -*- coding:utf-8 -*-
#

import re

"""
需求：
    在字符串中查找电话号码。你知道模式：3 个数字，一个短横线，3
个数字，一个短横线，再是4 个数字。例如：415-555-4242。

"""

"""
普通方式实现
"""


def isPhoneNumber(text):
    if len(text) != 12:
        return False;
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    else:
        return True


def is_phonenumber(msg):
    for i in range(len(msg)):
        chunk = msg[i: i + 12]  # 提供一个循环查找的方法
        if isPhoneNumber(chunk):
            print("找到电话号码： " + chunk)
    print("Done")
    return


"""
方式2：用正则表达式来实现
"""


def search_phonenumber_withre(txt):
    for i in range(len(txt)):
        chunk = txt[i:i + 12]
        if re.compile(r'\d{3}.\d{3}.\d{4}').search(chunk):
            print("找到电话号码: " + chunk)
    print("已查找到文本结尾！")


if __name__ == '__main__':
    msg = "Call me at 415-555-1011 tomorrow. 415-555/9999 is my office."
    is_phonenumber(msg)
    print("用正则查找：")
    search_phonenumber_withre(msg)
