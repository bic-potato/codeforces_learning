#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:06:06 2020

@author: zuoxichen
"""

def input_set():
    a=input()
    list0=a.split()
    set1=set(int(i) for i in list0)
    return(set1)

n=int(input())
set2=input_set()
set3=input_set()
set3.update(set2)
list2=[]
for i in range(1,n+1):
    if i in set3:
        list2.append('1')
    else:
        list2.append('')
        break

if all(list2) is True:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')