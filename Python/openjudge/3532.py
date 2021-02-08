#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:01:15 2020

@author: cage(ChenKaiqi, Zhejiang University)
"""
n = int(input())
a = list(map(int,input().split()))
b = [0]*len(a)
ans = 0
for i in range(len(a)):
    b[i] = a[i]
    for j in range(i):
        if a[j] < a[i]:
            b[i] = max(b[i],b[j] +a[i])
    ans = max(ans,b[i])
print(ans)