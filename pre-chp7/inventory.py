#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': '12'}


def displayInventory(inventory):
    print("================>Inventory:")
    item_cnt = 0
    try:
        for k, v in inventory.items():
            print(str(v) + ' ' + k)
            item_cnt += v
        print("Total number of items: " + str(item_cnt))
    except TypeError as err:
        print("It's occar a TypeError,check inventory !")


def addToInventory(inventory, addedItems):
    pass

displayInventory(stuff)
