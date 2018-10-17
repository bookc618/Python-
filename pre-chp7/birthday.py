#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 

dat = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print("Enter a name(Blank to quit)")
    getName = input()
    if getName == '':
        break

    if getName in dat:
        print(getName + " 的生日：" + dat[getName])
    elif getName not in dat:
        print("Birthday not found,please enter something:", end='')
        bday = input()
        dat[getName] = bday
        print("Data updated!")
        for item in dat.items():
            print(item)
