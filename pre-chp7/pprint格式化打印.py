#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 实现简单的字符统计程序，并用pprint方法格式化输出

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for letter in message:
    count.setdefault(letter, 0)
    count[letter] += 1

#pprint.pprint(count)
print(pprint.pformat(count))
