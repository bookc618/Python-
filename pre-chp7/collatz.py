#!/usr/bin/python3
##
## file:practice1.py
## 描述：
#   编写一个名为 collatz()的函数,它有有一个名为 number 的参数。如果参数是偶数,那么 collatz()就打印出 number // 2,并返回该值。如果 number 是奇数,collatz()就打印并返回 3 * number + 1。然后编写一个程序,让用户输入一个整数,并不断对这个数调用 collatz(),直到函数返回值1 .
##

def collatz(number):
        if number%2 == 0:
            return number//2
        elif number%2 != 0:
            return 3*number+1

if __name__ == '__main__':
    print('请输入：',end='')
    try:
        getInfo=int(input())
        while getInfo > 0 and getInfo !=1 :
            z=collatz(getInfo)
            print(z,end=' ')
            getInfo=z
        print(' ')
    except ValueError:
        print('\t非法数字！')
