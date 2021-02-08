#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:11:16 2020

@author: zuoxichen
"""
import sys
def main_args():
    a=list(input())
    k=0
    n=0
    for i in a:
        n+=1
        if (i=='4' or i=='7'):
            k+=1
        else:
            k+=0
    return [n,k]

list1=main_args()
k=str(list1[1])
n=list1[0]
if n==int(k) and n!=1:
    print('YES')
    sys.exit(0)
else:
    for i in k :
        if i!='4' or i!='7':
            print('NO')
            sys.exit(0)
print('YES')
    