#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:41:57 2020

@author: zuoxichen
"""
a=input()
n=len(a)
i=0
j=0
while i<n-1:
    if a[i]==a[i+1]:
        j+=1
    else:
        j=0
    if j==6:
        print('YES')
        break
    i+=1
else:
    print('NO')