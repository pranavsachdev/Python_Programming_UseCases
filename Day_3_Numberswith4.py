# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 07:37:40 2019

@author: prana
"""


def count_if_four(num):
    present = 0
    for i in range(1, num+1):
        if (check_for_4(i) == True):
            present += 1
    return present

def check_for_4(x):
    while (x != 0):
        if (x%10 == 4):
            return True
        x = x // 10
    
# count_if_four(2000)
if __name__ == "__main__":
    for _ in range(int(input())):
        print(count_if_four(int(input())))
