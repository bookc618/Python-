#!/usr/bin/python3
##
##

import random

secrectNum = random.randint(1,20)
print("猜猜我是多少？")

for guessTaken in range(1,6):
	print("请输入：")
	getInput = int(input())

	if getInput < secrectNum:
		print("小了!")
	elif getInput > secrectNum:
		print("大了")
	else:
		break

if getInput == secrectNum:
	print("恭喜你！你在第 "+str(guessTaken) + "次猜中了数字 "+ str(secrectNum)) 
else:
	print("很遗憾，你一直没有猜中数字 "+ str(secrectNum))
