#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 

spam = {'Red': '41', 'Green': '42'}
print("please input you want to query data: ")
getInput = input()
print(spam.get(getInput, 0))
