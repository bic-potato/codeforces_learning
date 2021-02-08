#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:21:35 2020

@author: zuoxichen
"""
n=int(input())
i=0
list1=[]
while i<n:
    a=input()
    b=a.count('###')
    c=a.count('### ###')
    list1.append(int(b/2-c))
    i+=1
else:
    print(sum(list1))
    