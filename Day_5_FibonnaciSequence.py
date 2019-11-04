# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 07:54:10 2019

@author: prana
"""

def fib(n):
    
    fib_lst = [1,1]
    # Program to print fibonacci numbers
    for i in range(2, n):
        fib_lst.append(fib_lst[i-1]+fib_lst[i-2])
    #for j in range(len(fib_lst)):
    #    fib_lst = [' {0} '.format(elem) for elem in fib_lst]
    return(fib_lst)
    
#a = fib(10)
#for i in range(len(a)):
#    print(a[i], end = " ")
if __name__ == "__main__":
    for _ in range(int(input())):
        tst = fib(int(input()))
        for i in range(len(tst)):
            print(tst[i], end = " ")