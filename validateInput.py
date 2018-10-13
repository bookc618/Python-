#!/usr/bin/python3
#-*- coding:utf-8 -*-
# 

while True:
    print("Enter your age: ")
    getAge = input()
    if getAge.isdecimal():
        break
    else:
        print("Input a valid number pls!")

while True:
    print("Enter you password:")
    getPasswd = input()
    if getPasswd.isalnum():
        break
    print("The letter of password only have haver letters and numbers!")
