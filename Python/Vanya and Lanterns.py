#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:22:17 2020

@author: zuoxichen
"""
l1=list(int(i) for i in input().split())
l2=sorted(list(int(i) for i in input().split()))
l3=list()
i=0
l4=[]
max1=l2[0]
l4.append(max1)
if l1[0]>=2:
    while i<=l1[0]-2:
        l3.append(l2[i+1]-l2[i])
        i+=1
else:
    l3.append(l2[0])
l4.append(l1[1]-l2[l1[0]-1])
print(round(max(l3)/2 if max(l3)/2>max(l4) else max(l4),10))