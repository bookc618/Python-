#!/usr/bin/python3
# -*- coding:utf-8 -*-
#
'''
需求:
    编写一个名为printTable()的函数，它接受字符串的列表的列表，将它显示在组
    织良好的表格中，每列右对齐。假定所有内层列表都包含同样数目的字符串。
'''

import numpy as np


def printtable(tabledata):
    '''
        此函数通过numpy函数以矩阵转置方式实现需求目标。
    '''
    tempdata = np.transpose(tabledata).tolist()
    element = []
    maxcolwidth = 0
    for i in range(len(tempdata)):
        for j in range(len(tempdata[i])):
            element = tempdata[i][j]
            if len(element) > maxcolwidth:
                maxcolwidth = len(element)

    for i in range(len(tempdata)):
        for j in range(len(tempdata[i])):
            print(tempdata[i][j].rjust(maxcolwidth), end='')
        print()


if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    printtable(tableData)
