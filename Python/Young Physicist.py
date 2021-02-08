#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:10:54 2020

@author: zuoxichen
"""

n=int(input())
i=0
x=0
y=0
z=0
while i<n:
    a=input()
    l1=a.split()
    l2=list(int(i) for i in l1 )
    x+=l2[0]
    y+=l2[1]
    z+=l2[2]
    i+=1
else:
    if (x==0)and(y==0)and(z==0):
        print('YES')
    else:
        print('NO')