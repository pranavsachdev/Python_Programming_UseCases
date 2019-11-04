# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:43:23 2019

@author: prana
"""

def padovan_generator(n):
    p = [1,1,1]
    for i in range(3,n+1):
        p.append(p[i-3] + p[i-2])
    return(p%1000000007)
    
#padovan_generator(12)
if __name__ == "__main__":
    for _ in range(int(input())):
        print(padovan_generator(int(input())))