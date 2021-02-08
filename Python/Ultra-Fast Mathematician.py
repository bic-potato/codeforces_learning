#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:34:01 2020

@author: zuoxichen
"""

a=input()
b=input()
i=0
n=len(a)
m=str()
while i<n:
    if a[i]==b[i]:
        m+='0'
    else:
        m+='1'
    i+=1
print(m)