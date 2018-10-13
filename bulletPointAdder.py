#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = "*" + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
print("The text has copied, don't forget copy !")
