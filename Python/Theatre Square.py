#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:44:08 2020

@author: zuoxichen
"""
def main_args(a,b):
    if (a%b!=0):
        o=a//b+1
    else:
        o=a//b
    return o
a=input()
list1=list(a.split(' '))
m=int(list1[0])
n=int(list1[1])
a=int(list1[2])
length=main_args(m, a)
wide=main_args(n, a)
print(length*wide)