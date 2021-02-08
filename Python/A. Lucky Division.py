#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 22:25:46 2020

@author: zuoxichen
"""

a=int(input())
list1=[]
for i in [0,4,7]:
    for j in [0,4,7]:
        for m in [0,4,7]:
            q=i*100+j*10+m
            if q==0:
                continue
            else:
                if a%q==0:
                    list1.append(True)
                else:
                    list1.append(False)
if True in list1:
    print('YES')
else:
    print('NO')
                
